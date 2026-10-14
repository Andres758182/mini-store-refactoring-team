from mini_store.checkout import validate_checkout


def test_valid_checkout_is_accepted():
    assert validate_checkout(3, 750, "MX", "44100", "card") == (True, "ok")


def test_empty_cart_is_rejected():
    assert validate_checkout(0, 750, "MX", "44100", "card") == (
        False,
        "cart is empty",
    )


def test_too_many_items_are_rejected():
    assert validate_checkout(51, 750, "MX", "44100", "card") == (
        False,
        "too many items",
    )
