from fastapi import status
from src.controllers.registrable_controller import app


@app.get('/')
def root() -> object:
     return {
        'code': status.HTTP_200_OK,
        'success': True,
        'data': {
            'message': 'Odoo auth service is running correctly'
        }
    }
