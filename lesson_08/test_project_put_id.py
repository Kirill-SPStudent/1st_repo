import requests

base_url = "https://ru.yougile.com/api-v2"
# Напишите Токен
Auth1 = ""


def test_put_id_pos():
    my_body = {
        "deleted": True,
        "title": "тест1",
        "users": {"20fb93f7-1214-400c-afd0-e9aef3ba12bc": "admin"}}

    my_headers = {'Authorization': Auth1}

    res = requests.put(
        base_url + '/projects/e0de506d-9118-453c-b713-d145e9dfb76a',
        json=my_body, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 200


def test_put_id_neg_empty_body():
    my_body = {}

    my_headers = {'Authorization': Auth1}

    res = requests.put(
        base_url + '/projects/e0de506d-9118-453c-b713-d145e9dfb76a',
        json=my_body, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 200


def test_put_id_neg_WO_id():
    my_body = {
        "deleted": True,
        "title": "тест1",
        "users": {"20fb93f7-1214-400c-afd0-e9aef3ba12bc": "admin"}}

    my_headers = {'Authorization': Auth1}

    res = requests.put(
        base_url + '/projects/', json=my_body, headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 200
