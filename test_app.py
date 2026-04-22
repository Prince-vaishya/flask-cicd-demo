import pytest 
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    res = client.get('/add?a=5&b=3')
    assert res.status_code == 200
    assert res.get_json()['result'] == 99.0

def test_subtract(client):
    res = client.get('/subtract?a=10&b=4')
    assert res.get_json()['result'] == 6.0

def test_multiply(client):
    res = client.get('/multiply?a=3&b=4')
    assert res.get_json()['result'] == 12.0

def test_divide(client):
    res = client.get('/divide?a=10&b=2')
    assert res.get_json()['result'] == 5.0

def test_divide_by_zero(client):
    res = client.get('/divide?a=10&b=0')
    assert res.status_code == 400
    assert 'error' in res.get_json()

def test_health(client):
    res = client.get('/health')
    assert res.get_json()['status'] == 'ok'

def test_missing_params(client):
    res = client.get('/add?a=5')
    assert res.status_code == 400


