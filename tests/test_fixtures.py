def test_app_exists(app, client):
    assert app is not None


def test_client_exists(app, client):
    assert client is not None


def test_client_responsive(app, client):
    resp = client.get('/')
    assert resp.status_code == 200
