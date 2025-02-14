import requests

base_url = "https://ru.yougile.com/api-v2"


def test_auth():
    # Напишите логин и пароль
    creds = {
        'login': '',
        'password': ''}
    res = requests.post(base_url+'/auth/companies', json=creds)
    assert res.status_code == 200
