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


# --- Item count boundaries ---


def test_one_item_is_accepted():
    assert validate_checkout(1, 750, "MX", "44100", "card") == (True, "ok")


def test_fifty_items_is_the_maximum_accepted():
    assert validate_checkout(50, 750, "MX", "44100", "card") == (True, "ok")


def test_negative_item_count_is_treated_as_empty_cart():
    assert validate_checkout(-1, 750, "MX", "44100", "card") == (
        False,
        "cart is empty",
    )


# --- Subtotal ---


def test_zero_subtotal_is_rejected():
    assert validate_checkout(3, 0, "MX", "44100", "card") == (
        False,
        "subtotal must be positive",
    )


def test_smallest_positive_subtotal_is_accepted():
    assert validate_checkout(3, 0.01, "MX", "44100", "card") == (True, "ok")


# --- Country ---


def test_us_is_a_supported_country():
    assert validate_checkout(3, 750, "US", "90210", "card") == (True, "ok")


def test_unsupported_country_is_rejected():
    assert validate_checkout(3, 750, "CA", "44100", "card") == (
        False,
        "unsupported country",
    )


def test_country_code_is_case_sensitive():
    assert validate_checkout(3, 750, "mx", "44100", "card") == (
        False,
        "unsupported country",
    )


# --- Postal code ---


def test_empty_postal_code_is_rejected():
    assert validate_checkout(3, 750, "MX", "", "card") == (
        False,
        "postal code is required",
    )


def test_blank_postal_code_is_rejected():
    assert validate_checkout(3, 750, "MX", "   ", "card") == (
        False,
        "postal code is required",
    )


# --- Payment method ---


def test_paypal_is_a_supported_payment_method():
    assert validate_checkout(3, 750, "MX", "44100", "paypal") == (True, "ok")


def test_unsupported_payment_method_is_rejected():
    assert validate_checkout(3, 750, "MX", "44100", "cash") == (
        False,
        "unsupported payment method",
    )


# --- Validation order: the first failing rule wins ---


def test_empty_cart_is_reported_before_any_other_error():
    assert validate_checkout(0, 0, "CA", "", "cash") == (False, "cart is empty")


def test_too_many_items_is_reported_before_subtotal_error():
    assert validate_checkout(51, 0, "CA", "", "cash") == (False, "too many items")


def test_subtotal_error_is_reported_before_country_error():
    assert validate_checkout(3, 0, "CA", "", "cash") == (
        False,
        "subtotal must be positive",
    )


def test_country_error_is_reported_before_postal_code_error():
    assert validate_checkout(3, 750, "CA", "", "cash") == (
        False,
        "unsupported country",
    )


def test_postal_code_error_is_reported_before_payment_error():
    assert validate_checkout(3, 750, "MX", "", "cash") == (
        False,
        "postal code is required",
    )