"""Pricing rules for orders."""

def calculate_shipping(discounted_subtotal, country):
    """Return the shipping cost based on the discounted subtotal and country."""
    if country == "MX":
        if discounted_subtotal >= 1000:
            shipping = 0.0
        else:
            shipping = 99.0
    else:
        if discounted_subtotal >= 2000:
            shipping = 199.0
        else:
            shipping = 299.0
    return shipping


def calculate_discount(subtotal: float, customer_type: str, coupon_code: str | None) -> float:
    """Return the total discount based on customer type and coupons."""
    discount = 0.0

    if customer_type == "premium":
        discount = subtotal * 0.10
    elif customer_type == "employee":
        discount = subtotal * 0.15

    if coupon_code == "SAVE5":
        discount += subtotal * 0.05
    elif coupon_code == "SAVE20" and subtotal >= 1500:
        discount += subtotal * 0.20

    return discount


def calculate_order_total(
    subtotal: float,
    customer_type: str,
    coupon_code: str | None,
    country: str,
) -> float:
    """Return the final order total after discounts, tax, and shipping."""
    discount = calculate_discount(subtotal, customer_type, coupon_code)

    discounted_subtotal = subtotal - discount

    if discounted_subtotal < 0:
        discounted_subtotal = 0

    if country == "MX":
        tax = discounted_subtotal * 0.16
    else:
        tax = 0.0

    shipping = calculate_shipping(discounted_subtotal, country)

    return round(discounted_subtotal + tax + shipping, 2)
