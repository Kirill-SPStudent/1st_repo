import requests


base_url = "https://ru.yougile.com/api-v2"


def test_get_token():
    # Напишите логин и пароль
    creds = {
        'login': '',
        'password': '',
        'companyId': '870c1088-09d6-47ed-95e4-ddd3d8bfb363'}

    res = requests.post(base_url+'/auth/keys', json=creds)
    assert res.status_code == 201
