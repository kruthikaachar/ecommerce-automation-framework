from api.base_api_client import BaseAPIClient


class CartAPI(BaseAPIClient):

    def get_carts(self):
        return self.get("/carts")

    def get_cart(self, cart_id):
        return self.get(f"/carts/{cart_id}")

    def add_cart(self, user_id, products):
        return self.post(
            "/carts/add",
            json={
                "userId": user_id,
                "products": products
            }
        )
    from api.base_api_client import BaseAPIClient


class CartAPI(BaseAPIClient):

    def get_carts(self):
        return self.get("/carts")

    def get_cart(self, cart_id):
        return self.get(f"/carts/{cart_id}")

    def add_cart(self, user_id, products):
        return self.post(
            "/carts/add",
            json={
                "userId": user_id,
                "products": products
            }
        )