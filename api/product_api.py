from api.base_api_client import BaseAPIClient


class ProductAPI(BaseAPIClient):

    def get_products(self):
        return self.get("/products")

    def get_product(self, product_id):
        return self.get(f"/products/{product_id}")
    from api.base_api_client import BaseAPIClient


class ProductAPI(BaseAPIClient):

    def get_products(self):
        return self.get("/products")

    def get_product(self, product_id):
        return self.get(f"/products/{product_id}")