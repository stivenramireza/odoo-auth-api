from src.utils.secrets import (
    ODOO_URL,
    ODOO_DB,
    ODOO_USERNAME,
    ODOO_PASSWORD
)

from xmlrpc.client import ServerProxy


class OdooConnection:

    __instance = None
    uid = None

    def __init__(self) -> None:
        if OdooConnection.__instance is None:
            try:
                common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
                self.uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
                OdooConnection.__instance = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
                logger.info('Connected to Odoo database successfully')
            except DatabaseError as error:
                logger.error(f'Error to connect to Odoo database: {error}')
        else:
            raise Exception('You cannot create another Odoo connection')

    @staticmethod
    def get_instance() -> None:
        if not OdooConnection.__instance:
            OdooConnection()
        return OdooConnection.__instance

    def search_and_read(model: str, fields: list[str] = [], where: list[any] = [], limit: int = 10) -> None:
        self.get_instance().execute_kw(
            ODOO_DB, self.uid, ODOO_PASSWORD, 
            model, 'search_read', [[where]], 
            {'fields': fields, 'limit': limit}
        )

    def create(model: str, params: list[any] = []) -> None:
        self.get_instance().execute_kw(
            ODOO_DB, self.uid, ODOO_PASSWORD,
            model, 'create', params
        )
    
    def write(model: str, id: list[int] = [], params: list[any] = []) -> None:
        new_params = [int(id)]
        new_params.append(params)
        values: list[any] = []
        values.append(params)
        self.get_instance().execute_kw(
            ODOO_DB, self.uid, ODOO_PASSWORD,
            model, 'write', values
        )
