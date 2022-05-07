import os
from task.config.config import ProductionConfig, DevelopmentConfig

def get_config():
    mode = os.environ.get("FLASK_ENV")
    if mode == "production":
        config = ProductionConfig
    else:
        config = DevelopmentConfig
    return config

def register_config(app):
    config = get_config()
    app.config.from_object(config)