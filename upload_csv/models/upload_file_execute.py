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
        start_time = datetime.now()
        print "Start Time", start_time
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
            self.env.cr.execute("SELECT id FROM product_template WHERE name='%s'" % (product_name))
            search_product_name = self.env.cr.fetchone()
            # search_product_name = self.env['product.template'].search([('name','=',product_name)])
            browse_product_template_records = self.env['product.template'].sudo().browse(search_product_name)
            product_id = browse_product_template_records
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

            if product_id.id > 0:
                returned_search_list = self.search_list(name_list)
                self.update_records(browse_product_template_records,column_list,returned_search_list)
            else:
                returned_search_list = self.search_list(name_list)
                self.create_records(column_list,returned_search_list)
        print "End Time", datetime.now()
        end_time = datetime.now()
        difference_in_time = end_time - start_time
        print "Time Difference", difference_in_time

    def update_records(self,search_product_name,column_list,returned_search_list):
        # print column_list
        # print returned_search_list
        search_product_name.sudo().write({
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
        self.env['product.template'].sudo().create({
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
        self.env.cr.execute("SELECT id FROM product_category WHERE name='%s'" % (column_list[0]))
        get_categ_id = self.env.cr.fetchone()[0]
        # print "Route IDs ", column_list[1]
        multiple_route = column_list[1].split(',')
        # print multiple_route
        get_route_ids = []

        for each in multiple_route:
            # get_route_id = 0
            # print "Get Route IDs", get_route_ids
            # self.env.cr.execute("SELECT id FROM stock_location_route WHERE name='%s'" % (column_list[1]))
            # get_route_id = self.env.cr.fetchone()[0]
            self.env.cr.execute("SELECT id FROM stock_location_route WHERE name='%s'" % (each))
            get_route_id = self.env.cr.fetchone()[0]
            # print "get_route_id",get_route_id
            get_route_ids.append(get_route_id)
        # print "Get Route IDs", get_route_ids

        self.env.cr.execute("SELECT id FROM account_account WHERE name='%s'" % (column_list[2]))
        get_income_account_id = self.env.cr.fetchone()[0]

        self.env.cr.execute("SELECT id FROM account_account WHERE name='%s'" % (column_list[3]))
        get_expense_account_id = self.env.cr.fetchone()[0]

        self.env.cr.execute("SELECT id FROM account_account WHERE name='%s'" % (column_list[4]))
        get_stock_account_input_id = self.env.cr.fetchone()[0]

        self.env.cr.execute("SELECT id FROM account_account WHERE name='%s'" % (column_list[5]))
        get_stock_account_output_id = self.env.cr.fetchone()[0]


        # get_categ_id = self.env['product.category'].search([('name', '=', column_list[0])]).id
        # get_route_id = self.env['stock.location.route'].search([('name', '=', column_list[1])]).id
        # get_income_account_id = self.env['account.account'].search([('name', '=', column_list[2])]).id
        # get_expense_account_id = self.env['account.account'].search([('name', '=', column_list[3])]).id
        # get_stock_account_input_id = self.env['account.account'].search([('name', '=', column_list[4])]).id
        # get_stock_account_output_id = self.env['account.account'].search([('name', '=', column_list[5])]).id
        search_list.extend([get_categ_id,
                            get_route_ids,
                            get_income_account_id,
                            get_expense_account_id,
                            get_stock_account_input_id,
                            get_stock_account_output_id])
        return search_list
