from openerp.report import report_sxw

class session(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(session, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_email': self.get_email,
        })
        
    def get_email(self, uid):
        return self.pool.get('res.users').browse(self.cr, self.uid, uid).email
    
report_sxw.report_sxw('report.openacademy.session', 'openacademy.session', 'addons/openacademy/report/session.rml',parser=session,header=True)
report_sxw.report_sxw('report.webkit_openacademy.session', 'openacademy.session', 'addons/openacademy/report/session.mako',parser=session,header=True)