from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

def test_list_notes():
    client = app.test_client()
    response = client.get("/notes")


    assert response.status.code == 200

def test_list_notes():
    client = app.test_client()
    response = client.get("/notes")

    assert response.status_code == 200
    assert response.get_json() == {"notes": []}


def test_create_note():
    client = app.test_client()
    response = client.post("/notes", json={"content": "Catatan pengujian"})

    assert response.status_code == 201
    assert response.get_json()["note"]["content"] == "Catatan pengujian"

def test_create_empty_note():
    client = app.test_client()
    response = client.post("/notes", json={"content": ""})

    assert response.status_code == 400