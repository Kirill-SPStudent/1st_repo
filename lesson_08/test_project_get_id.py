import requests

base_url = "https://ru.yougile.com/api-v2"
# Напишите Токен
Auth1 = ""


def test_get_id_pos():

    my_headers = {'Authorization': Auth1}

    res = requests.get(
        base_url + '/projects/e0de506d-9118-453c-b713-d145e9dfb76a',
        headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 200


def test_get_id_neg_WO_projects():

    my_headers = {'Authorization': Auth1}

    res = requests.get(
        base_url + 'e0de506d-9118-453c-b713-d145e9dfb76a',
        headers=my_headers)
    assert res.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert res.status_code == 200


def test_get_id_neg_empty_ContType():

    my_headers = {'Authorization': Auth1}

    res = requests.get(
        base_url + '/projects/e0de506d-9118-453c-b713-d145e9dfb76a',
        headers=my_headers)
    assert res.headers["Content-Type"] == ''
    assert res.status_code == 200
