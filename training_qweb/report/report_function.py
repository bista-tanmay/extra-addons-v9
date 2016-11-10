
from openerp.osv import osv
from openerp.report import report_sxw
from datetime import datetime

class TrainingReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(TrainingReport, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                    'get_current_time':self.get_current_time,
                    'get_data':self.get_data,
            })

    def get_current_time(self):
        current_time=datetime.now()
        print"current_timecurrent_timecurrent_time",current_time
        return current_time

    def get_data(self):
        return "<p>Sale Order</p>"

class ReportTrainingQwb(osv.AbstractModel):
    #    name must be report.module_name.template_id
    _name='report.training.report_sale_order_qweb'
    _inherit ='report.abstract_report'
    _template = 'training.report_sale_order_qweb'
    _wrapped_report_class = TrainingReport