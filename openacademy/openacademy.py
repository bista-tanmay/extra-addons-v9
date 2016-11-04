from openerp.osv import osv, fields
import time
from openerp.tools.translate import _

class openacademy_course(osv.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'responsible_id': fields.many2one('res.users', 'Responsible', required=True),
        'session_ids': fields.one2many('openacademy.session', 'course_id',  'Session'),
        'description': fields.text('Description')
    }
    
    def name_get(self, cr, uid, ids, context=None):
        res = []
        for course in self.read(cr, uid, ids, ['name', 'responsible_id']):
            name = course['name'] + '('+ course['responsible_id'][1] + ')'
            res.append((course['id'], name))
        return res

    def _check_description(self, cr, uid, ids, context=None):
        for course in self.browse(cr, uid, ids, context=context):
            if course.name == course.description:
                return False
        return True

    _constraints = [(_check_description, _("Name and Description can not be same!!!"), ['name', 'description'])]
    _sql_constraints = [('name_unique', 'unique(name)', _('Name must be unique!!'))]

class openacademy_session(osv.Model):

    def _get_attendee_count(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        for session in self.browse(cr, uid, ids, context=context):
            res[session.id] = len(session.attendee_ids)
        return res

    def _get_remaining_seats(self, cr, uid, ids, field_name , args, context=None):
        res = {}
        for session in self.browse(cr, uid, ids, context=context):
            res[session.id] = session.seats and (100*(session.seats - len(session.attendee_ids)))/session.seats or 0
        return res

    _name = 'openacademy.session'
    _inherit = ['mail.thread','ir.needaction_mixin']
    _description = 'Session'
    _columns = {
        'course_id': fields.many2one('openacademy.course', 'Course', 
                                           ondelete='cascade', required=True),
        'order_id': fields.many2one('sale.order', 'Order'),
        'active': fields.boolean('Active'),
        'duration': fields.float('Duration'),
        'instructor_id': fields.many2one('res.partner', 'Instructor', required=True, domain=[('instructor','=',True)], track_visibility="always"),
        'name': fields.char('Name', size=64, required=True),
        'seats': fields.integer('Seats'),
        'start_date': fields.date('Start Date'),
        'state': fields.selection([('draft', 'Draft'),
                                    ('confirm', 'Open'),
                                    ('done', 'Done'),
                                    ('cancel', 'Cancel'),
                                    ('delay', 'Delay')
                                    ], 'Status', track_visibility="onchange"),
        'attendee_ids': fields.one2many('openacademy.attendee', 'session_id', 'Attendee'),
        'attendee_count': fields.function(_get_attendee_count, string="No of Attendee", type="integer", store=True),
        'remaining_seats_count': fields.function(_get_remaining_seats, string="Available Seats", type="integer", store=True),
        'color': fields.integer('Color Index')

    }
    _defaults = {
        'active': True,
        'start_date': time.strftime('%Y-%m-%d'),
        'state': 'draft',
        'color': 0,
       # 'name':  lambda self, cr, uid, context: self.pool.get('ir.sequence').get(cr, uid, 'openacademy.session'), 
    }

    def _needaction_domain_get(self, cr, uid, context=None):
        """ Returns the domain to filter records that require an action
            :return: domain or False is no action
        """
        return [('state','=','confirm')]
        
    def copy(self, cr,uid, id, default=None, context=None):
        session = self.browse(cr, uid, id, context=context)
        name = _("Copy of %s")%session.name
        default['name'] = name
        default['attendee_ids'] = []
        return super(openacademy_session, self).copy(cr, uid, id, default=default, context=context)
        
    def on_change_seats(self, cr, uid, ids, seats, attendee_ids):
        remaining_seats = seats and (100*(seats - len(attendee_ids)))/seats or 0
        warning = {}
        if seats < 0:
            warning = {'title': _('Warning!!!'),
                        'message': _('Seats cannot be negative')
                    }
        return {'value': {'remaining_seats_count': remaining_seats}, 'warning': warning} 

    def action_confirm(self, cr, uid, ids, context=None):
        self.message_post(cr, uid, ids, body=_("Session is <b>Confirmed</b>"))
        return self.write(cr, uid, ids, {'state': 'confirm'})

    def action_delay(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'delay'})

    def action_cancel(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'})

    def action_done(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'done'})


class openacademy_attendee(osv.Model):
    _name = "openacademy.attendee"
    _description="Attendee"
    _columns = {
        'session_id': fields.many2one('openacademy.session', 'Session', ondelete='cascade'),
        'name': fields.char('Name', size=64, required=True),
        'partner_id': fields.many2one('res.partner', 'Attendee')
    }
    _sql_constraints = [('session_partner_unique', 'unique(session_id,partner_id)', _('partner must be unique per session!!'))]
    
class res_partner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
        'instructor': fields.boolean('Instructor')
    }
    
