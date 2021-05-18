from fastapi import HTTPException, status

from src.repositories import user_repository
from src.utils.validators import is_correct_email


def find_users() -> list[dict[str, any]]:
    return user_repository.find_users()


def save(user: dict[str, any]) -> None:
    if not user['name'] or not user['email'] or not user['password'] or not user['identification'] or not user['phone']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mising param 'name', 'email', 'password', 'identification' or 'phone'")
    elif len(password) < 6: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Password too short')
    elif len(identification) < 5: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Identification too short')
    elif len(phone) < 6: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Phone too short')
    elif not is_correct_email(email): 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid email. Try again.')
    user_repository.save(user)
