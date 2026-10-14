"""Checkout validation rules."""

MAX_ITEMS = 50
SUPPORTED_COUNTRIES = {"MX", "US"}
SUPPORTED_PAYMENT_METHODS = {"card", "paypal"}


def validate_checkout(
    item_count: int,
    subtotal: float,
    country: str,
    postal_code: str,
    payment_method: str,
) -> tuple[bool, str]:
    """Validate whether an order may proceed to checkout."""
    # "not x > 0" (instead of "x <= 0") also rejects NaN, like the original code.
    if not item_count > 0:
        return False, "cart is empty"
    if item_count > MAX_ITEMS:
        return False, "too many items"
    if not subtotal > 0:
        return False, "subtotal must be positive"
    if country not in SUPPORTED_COUNTRIES:
        return False, "unsupported country"
    if not postal_code.strip():
        return False, "postal code is required"
    if payment_method not in SUPPORTED_PAYMENT_METHODS:
        return False, "unsupported payment method"
    return True, "ok"