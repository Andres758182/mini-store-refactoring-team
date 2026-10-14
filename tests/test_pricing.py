from mini_store.pricing import calculate_order_total


def test_standard_customer_in_mexico_pays_tax_and_shipping():
    assert calculate_order_total(500, "standard", None, "MX") == 679.0


def test_premium_customer_receives_discount():
    assert calculate_order_total(1000, "premium", None, "MX") == 1143.0


def test_save20_coupon_requires_minimum_subtotal():
    assert calculate_order_total(1400, "standard", "SAVE20", "MX") == 1624.0
