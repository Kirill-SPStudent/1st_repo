import requests

base_url = "https://ru.yougile.com/api-v2"
# Напишите Токен
Auth1 = ""


def test_create_pos():

    creds = {
        "title": "тест1",
        "users": {"20fb93f7-1214-400c-afd0-e9aef3ba12bc": "admin"}}

    my_headers = {'Authorization': Auth1}

    res = requests.post(
        base_url + '/projects', json=creds, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 201


def test_create_neg_empty_headers():

    creds = {
        "title": "тест1",
        "users": {"20fb93f7-1214-400c-afd0-e9aef3ba12bc": "admin"}}

    my_headers = {}

    res = requests.post(
        base_url + '/projects', json=creds, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 201


def test_create_neg_WO_Tytle():

    creds = {
        "title": "",
        "users": {"20fb93f7-1214-400c-afd0-e9aef3ba12bc": "admin"}}

    my_headers = {'Authorization': Auth1}

    res = requests.post(
        base_url + '/projects', json=creds, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 201
