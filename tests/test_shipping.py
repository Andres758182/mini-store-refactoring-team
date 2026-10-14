from mini_store.shipping import chargeable_weight, shipping_quote


def test_chargeable_weight_uses_real_weight_when_it_is_higher():
    assert chargeable_weight(10, 20, 20, 20) == 10


def test_domestic_shipping_quote_uses_billable_weight():
    assert shipping_quote(2, 50, 40, 30, "MX", False) == 305.0


def test_expedited_shipping_adds_surcharge():
    assert shipping_quote(2, 50, 40, 30, "MX", True) == 411.75
