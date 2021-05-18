from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.services import user_service
from src.models.user_model import User
from src.utils.logger import logger


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def get_user() -> dict[str, any]:
    return {
        'code': status.HTTP_200_OK,
        'success': True,
        'data': {
            'message': 'Odoo auth service is running correctly'
        }
    }


@app.get('/users')
def get_user() -> dict[str, any]:
    return {
        'code': status.HTTP_200_OK,
        'success': True,
        'data': user_service.find_users()
    }


@app.post('/signup')
def create_user(user: User) -> dict[str, any]:
    try:
        user_service.save(user.to_dict())
        return {
            'code': status.HTTP_200_OK,
            'success': True,
            'data': {
                'message': 'User has been created successfully'
            }
        }
    except Exception as error:
        return error
