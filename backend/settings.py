from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str

    CORS_ALLOWED_ORIGINS: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int 
    POSTGRES_DB: str 
    POSTGRES_USER: str 
    POSTGRES_PASSWORD: str 

    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: int

    SUPERADMIN_ID: str
    SUPERADMIN_FIRST_NAME: str
    SUPERADMIN_LAST_NAME: str
    SUPERADMIN_LOGIN: str
    SUPERADMIN_PHONE: str
    SUPERADMIN_EMAIL: str
    SUPERADMIN_PASSWORD: str

    def build_postgres_dsn(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    
    def build_redis_dsn(self) -> str:
        return (
            f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        )

    class Config:
        env_file = '.env.local'



settings = Settings()