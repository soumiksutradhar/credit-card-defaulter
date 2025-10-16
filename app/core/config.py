from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    ENVIRONMENT: str = "development"	# default string value "development provided here in case a default value is not given in .env file 

    @property
    def DATABASE_URL(self) -> str:	# constructs a PostgreSQL database URL
        return (
            f"postgresql+psycopg2://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )

    class Config:
        env_file = ".env"   # tells Pydantic where to look for env vars


@lru_cache()
def get_settings() -> Settings:	# cache the settings so they're only loaded once
    return Settings()
