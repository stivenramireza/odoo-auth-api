import xmlrpc.client

info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()

url, db, username, password = info['host'], info['database'], info['user'], info['password']
