from uvicorn import Server, Config
from configuration.configuration import app_config
from fastapi import FastAPI
from configuration.injection import Container
from source.apis.etl_pipeline_router import app_router


def create_app() -> FastAPI:
    # Initialize the FastAPI
    app = FastAPI(title="ETL pipeline microservice",
                  description="Swagger of the data egineering task")
    # Injection
    container = Container()
    # Including apis to the app
    app.container = container
    app.include_router(app_router, tags=["ETL pipeline"])
    return app


app = create_app()


@app.on_event("startup")
async def create_db():
    container = Container()
    db = container.db()
    db.create_database()


if __name__ == '__main__':
    server = Server(Config(app=app,
                           host=app_config.APP_HOST,
                           port=app_config.APP_PORT))
    server.run()
