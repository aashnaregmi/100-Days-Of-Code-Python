from fastapi import Request
from datetime import datetime


def register_middleware(app):
    @app.middleware("http")
    async def log_request(request: Request, call_next):

        start_time = datetime.now()

        print("=" * 40)

        print(f"Started At   : {start_time}")
        print("." * 40)

        response = await call_next(request)

        end_time = datetime.now()

        print(f"Finished At  : {end_time}")
        print(f"Status Code  : {response.status_code}")
        print("=" * 40)

        return response
