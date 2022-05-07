from flask_restx import  marshal
from task.api.task.model import TaskModel
from task.api.task.schema import TaskSchema
from task.extension.database_extension import db


class TaskService:
    def __init__(self, api):
        self.api = api
        
    def get_all(self) -> list:
        result = TaskModel.query.all()
        response = marshal(result, TaskSchema.get_response(self.api))
        return response
    
    def insert(self, data):
        tasks_model = TaskModel(name=data['name'])
        db.session.add(tasks_model)
        db.session.flush() 
        db.session.commit()

        response = marshal(tasks_model, TaskSchema.post_response(self.api))
        return response

    def update(self, id, data):
        task = TaskModel.query.filter_by(id=id).first()
        if not task:
            return task
        task.name = data['name']
        task.status = data['status']
        task.id = data['id']
        db.session.commit()
        return task
    
    def delete(self, id):
        task = TaskModel.query.filter(TaskModel.id == id)
        if not task:
            return task
        response = task.delete()
        db.session.commit()
        return response