from re import search

from openerp import fields, models,api,_
import xlrd
import base64
from datetime import datetime

class UploadFile(models.TransientModel):
    _name = 'upload.file'

    upload_file = fields.Binary("Choose Excel File")

    @api.multi
    def upload_excel_file(self):
        print "Start Time: ",datetime.now()
        file_datas = base64.b64decode(self.upload_file)
        each_file = open('/home/bista/Downloads/data.xlsx', "w")
        each_file.write(file_datas)
        each_file.close()
        workbook = xlrd.open_workbook('/home/bista/Downloads/data.xlsx')
        sheet = workbook.sheet_by_index(0)
        can_be_sold = True
        can_be_purchased = True
        active = True
        for i in range(1,sheet.nrows):
            if sheet.row_values(i)[0] == '':
                continue
            if sheet.row_values(i)[2] == '':
                continue
            if sheet.row_values(i)[5] == '':
                continue
            search_results = self.env['product.template'].search([('name','=',sheet.row_values(i)[0])])
            browse_records = self.env['product.template'].browse(search_results.id)
            product_id = browse_records.id
            if product_id > 0:
                category_name = sheet.row_values(i)[2]
                get_product_type = sheet.row_values(i)[5]
                get_costing_method = sheet.row_values(i)[8]
                route_name = sheet.row_values(i)[10]
                get_inventory_evaluation = sheet.row_values(i)[11]
                income_account_name = sheet.row_values(i)[12]
                expense_account_name = sheet.row_values(i)[13]
                product_type = 'product'
                costing_method = 'standard'
                inventory_evaluation = 'real_time'

                if sheet.row_values(i)[3] == 'N':
                    can_be_sold = False
                if sheet.row_values(i)[4] == 'N':
                    can_be_purchased = False
                if sheet.row_values(i)[6] == 'N':
                    active = False
                if get_product_type == 'Stockable Product':
                    product_type = 'product'
                elif get_product_type == 'Consumable':
                    product_type = 'consu'
                elif get_product_type == 'Service':
                    product_type = 'service'
                if get_costing_method == 'Standard Price':
                    costing_method = 'standard'
                elif get_costing_method == 'Average Price':
                    costing_method = 'average'
                elif get_costing_method == 'Real Price':
                    costing_method = 'real'
                if get_inventory_evaluation == 'Periodic (manual)':
                    inventory_evaluation = 'manual_periodic'
                elif get_inventory_evaluation == 'Perpetual (automated)':
                    inventory_evaluation = 'real_time'

                get_categ_id = self.env['product.category'].search([('name', '=', category_name)])
                get_route_id = self.env['stock.location.route'].search([('name','=',route_name)])
                get_income_account_id = self.env['account.account'].search([('name','=',income_account_name)])
                get_expense_account_id = self.env['account.account'].search([('name','=',expense_account_name)])

                browse_records.write({
                     'description':sheet.row_values(i)[1],
                     'categ_id': get_categ_id.id,
                     'type': product_type,
                     'active': active,
                     'sale_ok': can_be_sold,
                     'purchase_ok': can_be_purchased,
                     'default_code': sheet.row_values(i)[7],
                     'property_cost_method': costing_method,
                     'standard_price': int(sheet.row_values(i)[9]),
                     'property_valuation': inventory_evaluation,
                     'route_ids': [(6, 0, [get_route_id.id])],
                     'property_account_income_id': get_income_account_id.id,
                     'property_account_expense_id': get_expense_account_id.id,
                     'property_stock_account_input': get_income_account_id.id,
                     'property_stock_account_output': get_expense_account_id.id,
                })
                # self.update_product(browse_records,i,sheet)
            else:
                product_name = sheet.row_values(i)[0]
                description = sheet.row_values(i)[1]
                category_name = sheet.row_values(i)[2]
                get_product_type = sheet.row_values(i)[5]
                get_costing_method = sheet.row_values(i)[8]
                route_name = sheet.row_values(i)[10]
                get_inventory_evaluation = sheet.row_values(i)[11]
                income_account_name = sheet.row_values(i)[12]
                expense_account_name = sheet.row_values(i)[13]
                product_type = 'product'
                costing_method = 'standard'
                inventory_evaluation = 'real_time'

                if sheet.row_values(i)[3] == 'N':
                    can_be_sold = False
                if sheet.row_values(i)[4] == 'N':
                    can_be_purchased = False
                if sheet.row_values(i)[6] == 'N':
                    active = False
                if get_product_type == 'Stockable Product':
                    product_type = 'product'
                elif get_product_type == 'Consumable':
                    product_type = 'consu'
                elif get_product_type == 'Service':
                    product_type = 'service'
                if get_costing_method == 'Standard Price':
                    costing_method = 'standard'
                elif get_costing_method == 'Average Price':
                    costing_method = 'average'
                elif get_costing_method == 'Real Price':
                    costing_method = 'real'
                if get_inventory_evaluation == 'Periodic (manual)':
                    inventory_evaluation = 'manual_periodic'
                elif get_inventory_evaluation == 'Perpetual (automated)':
                    inventory_evaluation = 'real_time'

                get_categ_id = self.env['product.category'].search([('name', '=', category_name)])
                get_route_id = self.env['stock.location.route'].search([('name', '=', route_name)])
                get_income_account_id = self.env['account.account'].search([('name', '=', income_account_name)])
                get_expense_account_id = self.env['account.account'].search([('name', '=', expense_account_name)])
                self.env['product.template'].create({
                    'name': product_name,
                    'description': description,
                    'categ_id': get_categ_id.id,
                    'type': product_type,
                    'active': active,
                    'sale_ok': can_be_sold,
                    'purchase_ok': can_be_purchased,
                    'default_code': sheet.row_values(i)[7],
                    'property_cost_method': costing_method,
                    'standard_price': int(sheet.row_values(i)[9]),
                    'property_valuation': inventory_evaluation,
                    'route_ids': [(6, 0, [get_route_id.id])],
                    'property_account_income_id': get_income_account_id.id,
                    'property_account_expense_id': get_expense_account_id.id,
                    'property_stock_account_input': get_income_account_id.id,
                    'property_stock_account_output': get_expense_account_id.id,
                })
        print "End Time: ",datetime.now()