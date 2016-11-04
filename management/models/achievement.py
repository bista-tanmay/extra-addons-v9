import time
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp import models, fields, api, _ # v8
from datetime import datetime


class achievement(models.Model):
    _name = 'achievement'
    _rec_name = 'description'
    
    image = fields.Binary('Image')
    description = fields.Text('Description')
    student_id = fields.Many2one('student','Student')
    res_partner_id = fields.Many2one('res.partner','Customer')
    employee_information_id = fields.Many2one('employee.information','Employee')
    state = fields.Selection([('start', 'Start'),
                              # ('in_progress', 'In Progress'),
                              ('stop', 'Stop'),
                              ],default='start')
    start_time = fields.Datetime('Start Time')
    end_time = fields.Datetime('End Time')
    duration_of_event = fields.Char()

    # This function is triggered when the user clicks on the button 'Start Event'
    @api.one
    def start_event(self):
        # curr_date_time = datetime.today()
        # tti =datetime.context_timestamp(timestamp=datetime.datetime.now())
        # t = ti.timetuple()
        start = datetime.now()
        self.write({
            'state': 'start',
            'start_time': start,
            'duration_of_event':'',
        })

    # # This function is triggered when the user clicks on the button 'Set to started'
    # @api.one
    # def event_in_progress(self):
    #     self.write({
    #         'state': 'in_progress'
    #     })

    # This function is triggered when the user clicks on the button 'Stop Event'
    @api.one
    def end_event(self):
        begin_time = datetime.strptime(str(self.start_time), "%Y-%m-%d %H:%M:%S")
        stop_time = datetime.now()
        time_elapsed = stop_time - begin_time
        self.write({
            'state': 'stop',
            'end_time': stop_time,
            'duration_of_event': time_elapsed,
        })


class achievement_res_partner(models.Model):
    _inherit = 'res.partner'
    achievement_ids = fields.One2many('achievement','res_partner_id','Customer Achievements')

class achievement_employee_information(models.Model):
    _inherit = 'employee.information'
    achievement_ids = fields.One2many('achievement','employee_information_id','Emp Achievements')
    

   
