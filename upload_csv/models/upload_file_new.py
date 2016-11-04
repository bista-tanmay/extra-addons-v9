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
        print "Start Time", datetime.now()
        file_datas = base64.b64decode(self.upload_file)
        each_file = open('/home/bista/Downloads/data.xlsx', "w")
        each_file.write(file_datas)
        each_file.close()
        workbook = xlrd.open_workbook('/home/bista/Downloads/data.xlsx')
        sheet = workbook.sheet_by_index(0)
        for i in range(1, sheet.nrows):
            can_be_sold = True
            can_be_purchased = True
            active = True
            if sheet.row_values(i)[0] == '':
                continue
            if sheet.row_values(i)[2] == '':
                continue
            if sheet.row_values(i)[5] == '':
                continue
            product_name = sheet.row_values(i)[0]
            search_product_name = self.env['product.template'].search([('name', '=', product_name)])
            # browse_product_template_records = self.env['product.template'].browse(search_product_name.id)
            product_id = search_product_name.id
            description = sheet.row_values(i)[1]
            get_product_type = sheet.row_values(i)[5]
            internal_reference = sheet.row_values(i)[7]
            get_costing_method = sheet.row_values(i)[8]
            cost_price = float(sheet.row_values(i)[9])
            get_inventory_evaluation = sheet.row_values(i)[11]
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

            column_list = []
            column_list.extend([product_name,description,product_type,active,can_be_sold,can_be_purchased,internal_reference,costing_method,cost_price,inventory_evaluation])

            category_name = sheet.row_values(i)[2]
            route_name = sheet.row_values(i)[10]
            income_account_name = sheet.row_values(i)[12]
            expense_account_name = sheet.row_values(i)[13]
            stock_account_input_name = sheet.row_values(i)[14]
            stock_account_output_name = sheet.row_values(i)[15]
            name_list = []
            name_list.extend([category_name,
                                route_name,
                                income_account_name,
                                expense_account_name,
                                stock_account_input_name,
                                stock_account_output_name])

            if product_id > 0:
                returned_search_list = self.search_list(name_list)
                self.update_records(search_product_name,column_list,returned_search_list)
            else:
                returned_search_list = self.search_list(name_list)
                self.create_records(column_list,returned_search_list)
        print "End Time", datetime.now()

    def update_records(self,search_product_name,column_list,returned_search_list):
        # print column_list
        # print returned_search_list
        search_product_name.write({
            'description': column_list[1],
            'categ_id': returned_search_list[0],
            'type': column_list[2],
            'active': column_list[3],
            'sale_ok': column_list[4],
            'purchase_ok': column_list[5],
            'default_code': column_list[6],
            'property_cost_method': column_list[7],
            'standard_price': column_list[8],
            'property_valuation': column_list[9],
            'route_ids': [(6, 0, [returned_search_list[1]])],
            'property_account_income_id': returned_search_list[2],
            'property_account_expense_id': returned_search_list[3],
            'property_stock_account_input': returned_search_list[4],
            'property_stock_account_output': returned_search_list[5],

        })

    def create_records(self,column_list,returned_search_list):
        # print column_list
        # print returned_search_list
        self.env['product.template'].create({
            'name': column_list[0],
            'description': column_list[1],
            'categ_id': returned_search_list[0],
            'type': column_list[2],
            'active': column_list[3],
            'sale_ok': column_list[4],
            'purchase_ok': column_list[5],
            'default_code': column_list[6],
            'property_cost_method': column_list[7],
            'standard_price': column_list[8],
            'property_valuation': column_list[9],
            'route_ids': [(6, 0, [returned_search_list[1]])],
            'property_account_income_id': returned_search_list[2],
            'property_account_expense_id': returned_search_list[3],
            'property_stock_account_input': returned_search_list[4],
            'property_stock_account_output': returned_search_list[5],
        })

    def search_list(self,column_list):
        search_list = []
        get_categ_id = self.env['product.category'].search([('name', '=', column_list[0])]).id
        get_route_id = self.env['stock.location.route'].search([('name', '=', column_list[1])]).id
        get_income_account_id = self.env['account.account'].search([('name', '=', column_list[2])]).id
        get_expense_account_id = self.env['account.account'].search([('name', '=', column_list[3])]).id
        get_stock_account_input_id = self.env['account.account'].search([('name', '=', column_list[4])]).id
        get_stock_account_output_id = self.env['account.account'].search([('name', '=', column_list[5])]).id
        search_list.extend([get_categ_id,
                            get_route_id,
                            get_income_account_id,
                            get_expense_account_id,
                            get_stock_account_input_id,
                            get_stock_account_output_id])
        return search_list
