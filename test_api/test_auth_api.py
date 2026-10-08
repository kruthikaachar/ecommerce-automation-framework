def test_login_api_success(auth_api):

    response = auth_api.login(
        "emilys",
        "emilyspass"
    )

    assert response.status_code == 200

    response_data = response.json()

    assert "accessToken" in response_data

def test_login_api_invalid_credentials(auth_api):

    response = auth_api.login(
        "emilys",
        "wrongpass"
    )

    assert response.status_code == 400