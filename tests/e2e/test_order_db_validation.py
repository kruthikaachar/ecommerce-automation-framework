import pytest
from DB.db_helper import DBHelper


@pytest.fixture
def db():
    helper = DBHelper(":memory:")   # temporary in-memory DB, nothing saved to disk
    helper.create_tables()
    yield helper
    helper.close()


def test_order_saved_in_db(db):
    db.insert_customer(1, "Test User", "test@example.com")
    db.insert_order(101, 1, 29.99, "COMPLETED")

    order = db.get_order_by_id(101)

    assert order is not None
    assert order[1] == 1             # customer_id
    assert order[2] == 29.99         # total_amount
    assert order[3] == "COMPLETED"   # status   