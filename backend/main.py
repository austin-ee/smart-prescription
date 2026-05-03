from fastapi import FastAPI
from backend.api.routes import router


def create_app():
    app = FastAPI(title="Smart Prescription API", 
              version="1.0", 
              description="API for generating smart prescriptions based on drug schedules.")
    app.include_router(router, prefix="/api")
    return app

app = create_app()

if __name__ == "__main__":
    create_app()