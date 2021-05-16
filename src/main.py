from src.controllers.registrable_controller import app
from src.utils.secrets import PORT, PYTHON_ENV
from src.utils.logger import logger

import uvicorn


def main() -> None:
    logger.info(f'Odoo auth service running at port {PORT} in {PYTHON_ENV} mode')
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
