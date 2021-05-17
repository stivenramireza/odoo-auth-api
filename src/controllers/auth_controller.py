from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/api/auth')
def get_user() -> dict[str, any]:
     return {
        'code': status.HTTP_200_OK,
        'success': True,
        'data': {
            'message': 'Odoo auth service is running correctly'
        }
    }


@app.get('/api/auth/user')
def get_user() -> dict[str, any]:
     return {
        'code': status.HTTP_200_OK,
        'success': True,
        'data': {
            'name': 'Stiven Ramírez Arango',
            'email': 'stivenramireza@gmail.com',
            'phone': '3017179746'
        }
    }
