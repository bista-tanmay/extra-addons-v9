from openerp.osv import osv, fields

class openacademy_wiz(osv.osv_memory):
    _name = "openacademy.wiz"
    _description = "wizard for attendee"
    _columns = {
            'session_id': fields.many2one('openacademy.session', 'Session'),
            'wiz_attendee_ids': fields.one2many('wiz.openacademy.attendee', 'wiz_id', 'Attendee')
    }
    def default_get(self, cr, uid, fields, context=None):
        res= super(openacademy_wiz, self).default_get(cr, uid, fields, context=context)
        if 'session_id' in fields:
            res['session_id'] = context.get('active_id')
        return res
    
    def action_create_attendee(self, cr, uid, ids, context=None):
        wiz_id = self.browse(cr, uid, ids, context=None)[0]
        attendee_obj = self.pool.get('openacademy.attendee')
        for attendee in wiz_id.wiz_attendee_ids:
            new_attendee_id = attendee_obj.create(cr, uid, {'name': attendee.name, 'partner_id': attendee.partner_id.id, 'session_id':  wiz_id.session_id.id})
        return {}

class wiz_openacademy_attendee(osv.osv_memory):
    _name = "wiz.openacademy.attendee"
    _columns = {
        'name': fields.char('Name', size=64),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'wiz_id': fields.many2one('openacademy.wiz', 'Wizard')
    }
    