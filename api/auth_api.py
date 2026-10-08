from api.base_api_client import BaseAPIClient


class AuthAPI(BaseAPIClient):

    def login(self, username, password):
        return self.post(
            "/auth/login",
            json={
                "username": username,
                "password": password
            }
        )