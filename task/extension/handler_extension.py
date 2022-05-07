from flask import Blueprint
from flask_restx import Api

from task.api.task.task_api import api as task_api

def register_handler(app):
    blueprint = Blueprint('API', __name__)
    api = Api(
          blueprint,
          doc='/doc',
          title='Resource API',
          version='0.1.0',
          description='A description'
    )
    
    api.add_namespace(task_api)
   
    app.register_blueprint(blueprint)
