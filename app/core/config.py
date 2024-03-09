from pydantic import Field
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str = Field(..., env='DATABASE_URL')
    api_key: str = Field(..., env='API_KEY')

    class Config:
        env_file = '.env'


settings = Settings()
