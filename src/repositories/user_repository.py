from src.config.database import OdooConnection


odoo_conn = OdooConnection()


def find_users() -> list[dict[str, any]]:
    return odoo_conn.search_and_read('res.partner', ['id', 'name', 'country_id', 'vat', 'email'])


def save(user: dict[str, any]) -> None:
    print(f'user: {user}')
    odoo_conn.create('res.partner', [user])
