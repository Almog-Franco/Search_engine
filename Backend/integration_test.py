from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hello_get():
    res = client.get("/api/v1/")
    assert res.status_code == 200
    assert res.json()["data"] == "Welcome to my search engine, this is the response for the basic Get request"
    
def test_hello_post():
    res = client.post("/api/v1/")
    assert res.status_code == 200
    assert res.json()["data"] == "Welcome to my search engine, this is the response for the basic Post request"
    
def test_search_word():
    res = client.get("/api/v1/search/test/times/3")
    assert res.status_code == 200
    assert type(res.json()) == dict

def test_search_pic():
    res = client.get("/api/v1/photos/test/times/3")
    assert res.status_code == 200
    assert type(res.json()) == dict

def test_search_videos():
    res = client.get("/api/v1/videos/test/times/3")
    assert res.status_code == 200
    assert type(res.json()) == dict