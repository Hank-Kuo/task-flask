from flask import Flask
from task.extension.database_extension import register_database
from task.extension.handler_extension import register_handler 
from task.extension.config_extension import register_config 

def create_app():
    app = Flask(__name__)
    register_config(app)
    register_handler(app)
    register_database(app)

    return app
