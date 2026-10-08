from api.cart_api import CartAPI


def test_get_carts():

    cart_api = CartAPI("https://dummyjson.com")

    response = cart_api.get_carts()

    assert response.status_code == 200

    response_data = response.json()

    assert "carts" in response_data

def test_get_single_cart():

    cart_api = CartAPI("https://dummyjson.com")

    response = cart_api.get_cart(1)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == 1
    from api.cart_api import CartAPI


def test_get_carts():

    cart_api = CartAPI("https://dummyjson.com")

    response = cart_api.get_carts()

    assert response.status_code == 200

    response_data = response.json()

    assert "carts" in response_data
    assert len(response_data["carts"]) > 0


def test_get_single_cart():

    cart_api = CartAPI("https://dummyjson.com")

    response = cart_api.get_cart(1)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["id"] == 1
    def test_add_product_to_cart():

     cart_api = CartAPI("https://dummyjson.com")

    products = [
        {
            "id": 1,
            "quantity": 2
        }
    ]

    response = cart_api.add_cart(
        user_id=1,
        products=products
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["userId"] == 1
    assert len(response_data["products"]) > 0