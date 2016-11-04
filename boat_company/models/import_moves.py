import openerp
import xmlrpclib
import csv
from openerp import pooler, sql_db
from openerp.osv import osv

cFileName = 'boatimport.csv'



reader = csv.reader(open(cFileName,'rb'))

if reader:
    # If we get a good reader, we initialize the connection using xmlrpclib
    # User access credentials
    username = "tanboatcompany"
    pwd = "solutions"
    dbname = "boatcompany"

    # Call xmlrpclib.ServerProxy("IP Address")
    sock_common = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/common")
    # To Logon with given credentials
    uid = sock_common.login(dbname, username, pwd)
    # Open actual location of object
    sock = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/object")
    db, pool = pooler.get_db_and_pool(dbname)
    cr = db.cursor()

    # Lookup Stock Location
    # Use short name of warehouse here
    cStockLocation = 'BStoc'
    args = [('name','=',cStockLocation)]
    stock_id = sock.execute(dbname, uid, pwd, 'stock.location','search',args)
    print stock_id

    cStagingLocation = "Staging"
    args = [('name', '=', cStagingLocation)]
    staging_id = sock.execute(dbname, uid, pwd, 'stock.location', 'search', args)
    print staging_id

    picking_template = {
        'code':'internal',
    }

    picking_id = sock.execute(dbname, uid,pwd,'stock.move','create',picking_template)

    for row in reader:
        if row:
            ProductCode = row[0]
            args = [('default_code', '=', ProductCode)]
            product_id = sock.execute(dbname, uid, pwd, 'product.template', 'search', args)
            print product_id
        move_template = {

        }
else:
    print 'Cant open file'
