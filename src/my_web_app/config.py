from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "my-web-app"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    model_config = {"env_prefix": "MWA_"}


settings = Settings()
