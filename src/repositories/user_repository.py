from src.config.database import OdooConnection


odoo_conn = OdooConnection()


def get_contacts() -> list[dict[str, any]]:
    return odoo_conn.search_and_read('res.partner', ['id', 'name', 'country_id', 'vat', 'email'])
