import pytest
import requests


@pytest.fixture
def auth():
    login_url = "https://x-clients-be.onrender.com/auth/login"
    login_data = {
        "username": "donatello",
        "password": "does-machines"
    }
    response = requests.post(login_url, json=login_data)
    return response.json()["access_token"]


def test_create_employee(auth):
    url = "https://x-clients-be.onrender.com/employee"
    headers = {"Authorization": f"Bearer {auth}"}
    employee_data = {
        "name": "Kirill",
        "email": "treyser154rus@gmail.com",
    }
    response = requests.post(url, json=employee_data, headers=headers)

    assert response.status_code == 201


def test_required_fields_for_employee(auth):
    url = "https://x-clients-be.onrender.com/employee"
    headers = {"Authorization": f"Bearer {auth}"}
    response = requests.post(url, json={}, headers=headers)

    assert response.status_code == 422
    errors = response.json().get("errors", {})
    assert "name" in errors, "Name field error missing"
    assert "email" in errors, "Email field error missing"


if __name__ == "__main__":
    pytest.main()
