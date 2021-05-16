from dotenv import load_dotenv
from src.utils.logger import logger

import os

if PYTHON_ENV == 'production':
    dotenv_path = '.env'
    logger.info('Using production environment variables')
else:
    dotenv_path = '.env.dev'
    logger.info('Using development environment variables')

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception('env files do not exist')

load_dotenv(dotenv_path)

PORT = os.environ.get('PORT')
PYTHON_ENV = os.environ.get('PYTHON_ENV')

ODOO_URL = os.environ.get('ODOO_URL')
ODOO_DB = os.environ.get('ODOO_DB')
ODOO_USER = os.environ.get('ODOO_USER')
ODOO_PASS = os.environ.get('ODOO_PASS')
