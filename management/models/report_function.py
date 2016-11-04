from openerp.osv import osv
from openerp.report import report_sxw
from datetime import datetime

from pytz import timezone


class ManagementReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(ManagementReport, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                    'get_current_time':self.get_current_time,
                    'get_data':self.get_data,
            })

    def get_current_time(self):
        now_utc = datetime.now(timezone('UTC'))
        now_localtime = now_utc.astimezone(timezone('Asia/Calcutta'))
        current_localtime = now_localtime.strftime("%Y-%m-%d %H:%M:%S")
        print"Current Localtime",current_localtime
        return current_localtime

    def get_data(self):
        return "<p>Yup Surely The Methods Are Executing</p>"

class ReportManagementQweb(osv.AbstractModel):
    #    name must be report.module_name.template_id
    _name ='report.management.student_rec_report'
    _inherit = 'report.abstract_report'
    _template = 'management.student_rec_report'
    _wrapped_report_class = ManagementReport