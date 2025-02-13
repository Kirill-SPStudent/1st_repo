import requests


base_url = "https://ru.yougile.com/api-v2"
# Напишите Токен
Auth1 = ""


def test_projects_list_pos():
    # Напишите логин и пароль
    creds = {
        'login': '',
        'password': ''}

    my_headers = {'Authorization': Auth1}

    res = requests.get(base_url+'/projects', json=creds, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 200


def test_projects_list_neg_wrong_status_code():
    # Напишите логин и пароль
    creds = {
        'login': '',
        'password': ''}

    my_headers = {'Authorization': Auth1}

    res = requests.get(base_url+'/projects', json=creds, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 404


def test_projects_list_neg_empty_creds():
    creds = {}

    my_headers = {'Authorization': Auth1}

    res = requests.get(
        base_url+'/projects', json=creds, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 200
