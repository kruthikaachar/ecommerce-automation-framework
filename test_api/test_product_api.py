from api.product_api import ProductAPI


def test_get_products():

    product_api = ProductAPI("https://dummyjson.com")

    response = product_api.get_products()

    assert response.status_code == 200

    response_data = response.json()

    assert "products" in response_data

    assert len(response_data["products"]) > 0

def test_get_single_product():

    product_api = ProductAPI("https://dummyjson.com")

    response = product_api.get_product(1)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == 1
    from api.product_api import ProductAPI


def test_get_products():

    product_api = ProductAPI("https://dummyjson.com")

    response = product_api.get_products()

    assert response.status_code == 200

    response_data = response.json()

    assert "products" in response_data
    assert len(response_data["products"]) > 0


def test_get_single_product():

    product_api = ProductAPI("https://dummyjson.com")

    response = product_api.get_product(1)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == 1