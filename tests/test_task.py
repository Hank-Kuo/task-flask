import pytest
import json
from task.application import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        client = app.test_client()
        yield client

 
GET_EMPTY_DATA = []
MOCK_REQUEST_DATA = {"name": "買晚餐"}
MOCK_RESPONSE_DATA = {"id": 1, "name":"買晚餐" ,"status":0}
MOCK_UPDATE_RESPONSE_DATA = {"id": 1, "name":"買早餐" ,"status":1}

def test_get_empty_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json['result']  == GET_EMPTY_DATA

def test_post_tasks(client):
    response = client.post('/task', data=json.dumps(MOCK_REQUEST_DATA),  content_type='application/json')
    assert response.status_code == 200
    assert response.json['result']== MOCK_RESPONSE_DATA


def test_put_tasks(client):
    response = client.post('/task', data=json.dumps(MOCK_REQUEST_DATA),  content_type='application/json')
    assert response.status_code == 200
    assert response.json['result']  == MOCK_RESPONSE_DATA

    response = client.put('/task/1', data=json.dumps(MOCK_UPDATE_RESPONSE_DATA),  content_type='application/json')
    assert response.status_code == 200
    assert response.json['result']== MOCK_UPDATE_RESPONSE_DATA
    
    
def test_delete_tasks(client):
    response = client.post('/task', data=json.dumps(MOCK_REQUEST_DATA),  content_type='application/json')
    assert response.status_code == 200
    assert response.json['result']  == MOCK_RESPONSE_DATA

    response = client.delete('/task/1')
    assert response.status_code == 200

    
