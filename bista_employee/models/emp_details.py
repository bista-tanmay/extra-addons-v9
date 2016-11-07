from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
from datetime import datetime


class employee_details(models.Model):

    _inherit = 'res.partner'

    emp_id = fields.Char("Employee Id")
    emp_dept = fields.One2many('dept.dept','dept_id',string="Department")
    country_id = fields.Many2one('res.country', 'Country')
    # states_id=fields.Many2one(related='country_id.state_id.id', store=True)

    @api.model
    def create(self,vals):
        print "==================== Create Method Called ======================"
        res = super(employee_details, self).create(vals)
        print "========>> New Record Created ID \n",res
        print "========>> New Record Created Name \n", res.name
        return res

    @api.multi
    def display(self):
        print "================ Button Method Called ======================="
        print "======== self ",self
        print "======== name ",self.name
        res = self.env['res.partner']
        print "======== res ",res

    @api.model
    def search(self, arg, offset=0, limit=None, order=None, count=False):
        print " ==================== Search Method Called ==========================="
        res = super(employee_details, self).search(arg, offset=0 , limit=0, order='', count=count)
        # print "\n========== Recodset =  ",res                     #woring code
        # for record in res:                                        #woring code
        #     print "\n Name of Recordset  = > ",record.name        #woring code
        return res

    @api.multi
    def write(self,vals):

        print "======================== Write Method Called =============================="
        print "\n ==========>>>>>  Old Name = >",self.name
        # print "\n==========>>>>>>  New Name = >",vals['name']   #woring code
        res = super(employee_details, self).write(vals)
        # print "\n==========>>>>>>  New Name = >",vals.name
        return res

    @api.multi
    def department(self):
        print "\n============= department Button Called =================\n"
        for dept in self.emp_dept:
            print "Department  = ",dept.dept_name,"\n"
        return

class department(models.Model):

    _name='dept.dept'

    dept_id=fields.Many2one("res.partner")
    dept_name=fields.Char(string ="Department Name")


