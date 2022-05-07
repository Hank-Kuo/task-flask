from flask import request
from flask_restx import Resource, Namespace
from task.api.task.schema import TaskSchema
from task.api.task.service import TaskService

api = Namespace('task', description='task Endpoints')
service = TaskService(api)

@api.route('s')
class Task(Resource):
    @api.marshal_with(TaskSchema.get_response(api), envelope='result')
    def get(self):
        response = service.get_all()
        return response, 200
    
@api.route('')
class Task(Resource):
    @api.expect(TaskSchema.post_request(api))
    @api.marshal_with(TaskSchema.post_response(api), envelope='result')
    def post(self):
        req_data = request.get_json(force=True)
        response = service.insert(req_data)
        return response


@api.route('/<string:id>')
class Task(Resource):
    @api.expect(TaskSchema.put_request(api))
    @api.marshal_with(TaskSchema.put_response(api), envelope='result')
    def put(self, id):
        req_data = request.get_json(force=True)
        response = service.update(id, req_data)
        if not response:
            api.abort(400, "tasks not found")
        return response
    

    def delete(self, id):
        response = service.delete(id)
        if not response:
            api.abort(400, "tasks not found")
        return response