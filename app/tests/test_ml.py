from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success when input is valid."""
    response = client.post(
        '/predict',
        json={
            'user_name': str('PotShot'),
            'password': str('bang'),
            'user_ailment': str('tired, stressed'),
            'user_effect': str('awake, relaxed')
        }
    )
    body = response.json()
    assert response.status_code == 200
    assert body['prediction'] in [True, False]
    assert 0.50 <= body['probability'] < 1


def test_invalid_input():
    """Return 422 Validation Error when user_name is not a string"""
    response = client.post(
        '/predict',
        json={
            'user_name': str('PotShot'),
            'password': str('bang'),
            'user_ailment': str('tired, stressed'),
            'user_effect': str('awake, relaxed')
        }
    )
    body = response.json()
    assert response.status_code == 422
    assert 'x1' in body['detail'][0]['loc']
