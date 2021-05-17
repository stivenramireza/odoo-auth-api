from src.config.database import OdooConnection


def get_contacts() -> list[dict[str, any]]:
    return OdooConnection().search_and_read('res.partner', ['name', 'vat', 'email'], [], 5)
