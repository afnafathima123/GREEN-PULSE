import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_home_loads(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"GreenPulse" in r.data

def test_health_endpoint(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert b"ok" in r.data

def test_plant_detail(client):
    r = client.get("/plant/1")
    assert r.status_code == 200

def test_plant_not_found(client):
    r = client.get("/plant/9999")
    assert r.status_code == 404

def test_water_plant(client):
    r = client.get("/water/1", follow_redirects=True)
    assert r.status_code == 200

def test_add_plant(client):
    r = client.post("/add", data={
        "name": "Test Fern",
        "type": "Fern",
        "health": "75",
        "notes": "Test plant",
        "emoji": "🌿"
    }, follow_redirects=True)
    assert r.status_code == 200
    assert b"Test Fern" in r.data
