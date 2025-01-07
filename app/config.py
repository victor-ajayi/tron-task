from pydantic import computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_USER: str
    DB_PASSWORD: str = ""
    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str
    TRON_PRO_API_KEY: str

    @computed_field
    @property
    def postgres_url(self) -> str:
        return str(
            MultiHostUrl.build(
                scheme="postgresql+psycopg2",
                username=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT,
                path=self.DB_NAME,
            )
        )

    @computed_field
    @property
    def test_postgres_url(self) -> str:
        return str(
            MultiHostUrl.build(
                scheme="postgresql+psycopg2",
                username=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT,
                path="test",
            )
        )


settings = Settings()
