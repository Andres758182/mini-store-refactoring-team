"""Checkout validation rules."""


def validate_checkout(
    item_count: int,
    subtotal: float,
    country: str,
    postal_code: str,
    payment_method: str,
) -> tuple[bool, str]:
    """Validate whether an order may proceed to checkout."""
    if item_count > 0:
        if item_count <= 50:
            if subtotal > 0:
                if country in {"MX", "US"}:
                    if postal_code.strip():
                        if payment_method in {"card", "paypal"}:
                            return True, "ok"
                        else:
                            return False, "unsupported payment method"
                    else:
                        return False, "postal code is required"
                else:
                    return False, "unsupported country"
            else:
                return False, "subtotal must be positive"
        else:
            return False, "too many items"
    else:
        return False, "cart is empty"
