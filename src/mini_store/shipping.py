"""Shipping quotation rules."""

VOLUMETRIC_DIVISOR = 5000

SHIPPING_RATES = {
    "MX": (89.0, 18.0),
    "US": (199.0, 42.0),
}
INTERNATIONAL_RATE = (299.0, 65.0)

EXPEDITED_MULTIPLIER = 1.35
OVERSIZE_LIMIT_CM = 100
OVERSIZE_SURCHARGE = 120.0


def volumetric_weight(length_cm: float, width_cm: float, height_cm: float) -> float:
    return (length_cm * width_cm * height_cm) / VOLUMETRIC_DIVISOR


def chargeable_weight(
    weight_kg: float,
    length_cm: float,
    width_cm: float,
    height_cm: float,
) -> float:
    volume_weight = volumetric_weight(length_cm, width_cm, height_cm)
    return max(weight_kg, volume_weight)


def _rates_for(destination_country: str) -> tuple[float, float]:
    return SHIPPING_RATES.get(destination_country, INTERNATIONAL_RATE)


def _is_oversized(length_cm: float, width_cm: float, height_cm: float) -> bool:
    return max(length_cm, width_cm, height_cm) > OVERSIZE_LIMIT_CM


def shipping_quote(
    weight_kg: float,
    length_cm: float,
    width_cm: float,
    height_cm: float,
    destination_country: str,
    expedited: bool,
) -> float:
    billable = chargeable_weight(weight_kg, length_cm, width_cm, height_cm)
    base, per_kg = _rates_for(destination_country)

    total = base + billable * per_kg

    if expedited:
        total *= EXPEDITED_MULTIPLIER

    if _is_oversized(length_cm, width_cm, height_cm):
        total += OVERSIZE_SURCHARGE

    return round(total, 2)