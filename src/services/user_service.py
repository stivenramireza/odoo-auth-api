from src.repositories import user_repository


def get_contacts() -> list[dict[str, any]]:
    return user_repository.get_contacts()
