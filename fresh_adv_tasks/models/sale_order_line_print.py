import xlsxwriter
from openerp import fields,models,api,_
from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsx

class SaleOrderLinePrint(models.Model):
    _inherit= 'sale.order.line'
    _rec_name = 'order_id'

class PartnerXlsx(ReportXlsx):


    def generate_xlsx_report(self, workbook, data, sale_order_lines):
        report_name = _("Sales Order Line Report")
        workbook.set_properties({
            'title': 'Sale Order line Report',
            'subject': 'Report',
            'author': 'Odoo User',
            'company': 'OCA',
            'category': 'Sales',
            'comments': 'Created with Python and XlsxWriter'})
        sheet = workbook.add_worksheet(report_name[:31])
        bold = workbook.add_format({'bold': True})
        sheet.repeat_rows(0)
        sheet.set_header('&LSale Order Line &CReport&RCielo')
        sheet.write(0, 0, "Product Name", bold)
        sheet.write(0, 1, "Product Description", bold)
        sheet.write(0, 2, "Product Qty", bold)
        sheet.write(0, 3, "Qty Delivered", bold)
        sheet.write(0, 4, "Qty Invoiced", bold)
        sheet.write(0, 5, "Unit Price", bold)
        sheet.write(0, 6, "Taxes", bold)
        sheet.write(0, 7, "Subtotal", bold)
        sheet.set_footer('&LSale Order Line &CReport&RPages &P of &N')
        count = 1
        for obj in sale_order_lines:
            sheet.write(count, 0, obj.product_tmpl_id.name)
            sheet.write(count, 1, obj.name)
            sheet.write(count, 2, obj.product_uom_qty)
            sheet.write(count, 3, obj.qty_delivered)
            sheet.write(count, 4, obj.qty_invoiced)
            sheet.write(count, 5, obj.currency_id.symbol + " " + str(obj.price_unit))
            sheet.write(count, 6, obj.tax_id.name)
            sheet.write(count, 7, obj.currency_id.symbol + " " + str(obj.price_subtotal))
            count = count + 1
        del count


PartnerXlsx('report.res.partner.xlsx','sale.order.line')
