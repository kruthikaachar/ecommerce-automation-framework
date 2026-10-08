import requests


class BaseAPIClient:

    def __init__(self, base_url):

        self.base_url = base_url

        self.session = requests.Session()

    def get(
        self,
        endpoint,
        headers=None,
        params=None
    ):

        return self.session.get(
            f"{self.base_url}{endpoint}",
            headers=headers,
            params=params
        )

    def post(
        self,
        endpoint,
        json=None,
        headers=None
    ):

        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=json,
            headers=headers
        )

    def put(
        self,
        endpoint,
        json=None,
        headers=None
    ):

        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=json,
            headers=headers
        )

    def delete(
        self,
        endpoint,
        headers=None
    ):

        return self.session.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )