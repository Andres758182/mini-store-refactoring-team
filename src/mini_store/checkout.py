"""Checkout validation rules."""


def validate_checkout(
    item_count: int,
    subtotal: float,
    country: str,
    postal_code: str,
    payment_method: str,
) -> tuple[bool, str]:
    """Validate whether an order may proceed to checkout."""
    if item_count <= 0:
        return False, "cart is empty"
    if item_count > 50:
        return False, "too many items"
    if subtotal <= 0:
        return False, "subtotal must be positive"
    if country not in {"MX", "US"}:
        return False, "unsupported country"
    if not postal_code.strip():
        return False, "postal code is required"
    if payment_method not in {"card", "paypal"}:
        return False, "unsupported payment method"
    return True, "ok"