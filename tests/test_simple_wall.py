def test_simple_wall_with_callback(app, client):
    resp = client.get('/pr-one')
    assert resp.status_code == 503
    assert resp.data.decode('utf-8') == 'simple-wall'


def test_simple_wall_with_default_callback_and_custom_status(app, client):
    resp = client.get('/pr-two')
    assert resp.status_code == 307
    assert resp.data.decode('utf-8') == 'Temporarily unavailable'


def test_simple_wall_with_default_callback_and_status(app, client):
    resp = client.get('/pr-three')
    assert resp.status_code == 503
    assert resp.data.decode('utf-8') == 'Temporarily unavailable'
