"""Shipping quotation rules."""


def volumetric_weight(length_cm: float, width_cm: float, height_cm: float) -> float:
    return (length_cm * width_cm * height_cm) / 5000


def chargeable_weight(
    weight_kg: float,
    length_cm: float,
    width_cm: float,
    height_cm: float,
) -> float:
    volume_weight = volumetric_weight(length_cm, width_cm, height_cm)
    return max(weight_kg, volume_weight)


def shipping_quote(
    weight_kg: float,
    length_cm: float,
    width_cm: float,
    height_cm: float,
    destination_country: str,
    expedited: bool,
) -> float:
    billable = chargeable_weight(weight_kg, length_cm, width_cm, height_cm)

    if destination_country == "MX":
        base = 89.0
        per_kg = 18.0
    elif destination_country == "US":
        base = 199.0
        per_kg = 42.0
    else:
        base = 299.0
        per_kg = 65.0

    total = base + billable * per_kg

    if expedited:
        total *= 1.35

    if length_cm > 100 or width_cm > 100 or height_cm > 100:
        total += 120.0

    return round(total, 2)
