from types import SimpleNamespace
from unittest.mock import Mock

from mini_store.notifications import NotificationService


def make_customer(channel: str):
    return SimpleNamespace(
        name="Ana",
        preferred_channel=channel,
        email="ana@example.com",
        phone="+521234567890",
        device_id="device-1",
    )


def test_email_order_confirmation_is_sent():
    email = Mock()
    service = NotificationService(email, Mock(), Mock())

    service.send_order_confirmation(make_customer("email"), "A-100")

    email.send.assert_called_once_with(
        "ana@example.com",
        "Order A-100 confirmed",
        "Hello Ana, your order A-100 was confirmed.",
    )


def test_sms_shipping_update_is_sent():
    sms = Mock()
    service = NotificationService(Mock(), sms, Mock())

    service.send_shipping_update(make_customer("sms"), "A-100", "TRACK-9")

    sms.send.assert_called_once_with(
        "+521234567890",
        "Order A-100 shipped. Tracking: TRACK-9.",
    )
