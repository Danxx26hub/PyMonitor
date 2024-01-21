from pydantic_settings import BaseSettings
from functools import lru_cache


class devSettings(BaseSettings):
    """Settings for development environment"""

    app_name: str = "PyMonitor"
    bar_label_cpu: str = "CPU Usage:"
    bar_label_ram: str = "RAM Usage:"


class prodSettings(BaseSettings):
    """Settings for production environment"""

    app_name: str = "PyMonitor"
    bar_label_cpu: str = "CPU Usage:"
    bar_label_ram: str = "RAM Usage:"


@lru_cache()
def get_settings(environment: str):
    """Return the settings for the given environment, loading in cache through lru_cache"""
    print(f"Loading {environment} settings")
    return devSettings() if environment == "dev" else prodSettings()
