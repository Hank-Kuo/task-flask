from flask_restx import fields

class TaskSchema:
    @staticmethod
    def get_response(api):
        get_response_payload = api.model("query task response payload", {
            "id": fields.Integer(),
            "name": fields.String(),
            "status": fields.Integer()
        })
        return get_response_payload
    
    @staticmethod
    def post_response(api):
        post_response_payload = api.model('create task response payload',{
            "id": fields.Integer(),
            "name": fields.String(),
            "status": fields.Integer()
        })
        return post_response_payload
    
    @staticmethod
    def post_request(api):
        post_request_payload = api.model('create task request payload', {
            'name': fields.String(required=True),
        })
        return post_request_payload

    @staticmethod
    def put_request(api):
        put_request_payload = api.model('update task request payload', {
            "id": fields.Integer(),
            "name": fields.String(),
            "status": fields.Integer()
        })
        return put_request_payload
    @staticmethod
    def put_response(api):
        put_response_payload = api.model('update task response payload', {
            "id": fields.Integer(),
            "name": fields.String(),
            "status": fields.Integer()
        })
        return put_response_payload