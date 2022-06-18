import os


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


class Configuration():
    DEBUG: bool = getenv_boolean("DEBUG")

    TOKEN_KEY: str = os.getenv("TOKEN_KEY", "")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_PORT: int = os.getenv("MYSQL_PORT", 3306)
    MYSQL_HOST: str = os.getenv("MYSQL_HOST")

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://"
        f"{MYSQL_USER}"
        f":{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}"
        f":{MYSQL_PORT}"
        f"/{MYSQL_DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
