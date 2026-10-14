"""Customer notification behavior."""

class NotificationService:
    def __init__(self, email_sender, sms_sender, push_sender):
        self.email_sender = email_sender
        self.sms_sender = sms_sender
        self.push_sender = push_sender

        self.Value_Error = ValueError("Unsupported notification channel")

    def send_order_confirmation_email(self, customer, order_id: str) -> None:
        subject = f"Order {order_id} confirmed"
        message = f"Hello {customer.name}, your order {order_id} was confirmed."
        self.email_sender.send(customer.email, subject, message)

    def send_order_confirmation_sms(self, customer, order_id: str) -> None:
        message = f"Order {order_id} confirmed for {customer.name}."
        self.sms_sender.send(customer.phone, message)

    def send_order_confirmation_push(self, customer, order_id: str) -> None:
        title = "Order confirmed"
        message = f"Order {order_id} is confirmed."
        self.push_sender.send(customer.device_id, title, message)

    def send_order_confirmation(self, customer, order_id: str) -> None:
        if customer.preferred_channel == "email":
            self.send_order_confirmation_email(customer, order_id)
        elif customer.preferred_channel == "sms":
            self.send_order_confirmation_sms(customer, order_id)
        elif customer.preferred_channel == "push":
            self.send_order_confirmation_push(customer, order_id)
        else:
            raise self.Value_Error

    def send_shipping_update_email(self, customer, order_id: str, tracking_code: str) -> None:
        subject = f"Order {order_id} shipped"
        message = (
            f"Hello {customer.name}, your order {order_id} shipped. "
            f"Tracking: {tracking_code}."
        )
        self.email_sender.send(customer.email, subject, message)

    def send_shipping_update_sms(self, customer, order_id: str, tracking_code: str) -> None:
        message = f"Order {order_id} shipped. Tracking: {tracking_code}."
        self.sms_sender.send(customer.phone, message)

    def send_shipping_update_push(self, customer, order_id: str, tracking_code: str) -> None:
        title = "Order shipped"
        message = f"Track order {order_id}: {tracking_code}."
        self.push_sender.send(customer.device_id, title, message)

    def send_shipping_update(self, customer, order_id: str, tracking_code: str) -> None:
        if customer.preferred_channel == "email":
            self.send_shipping_update_email(customer, order_id, tracking_code)
        elif customer.preferred_channel == "sms":
            self.send_shipping_update_sms(customer, order_id, tracking_code)
        elif customer.preferred_channel == "push":
            self.send_shipping_update_push(customer, order_id, tracking_code)
        else:
            raise self.Value_Error
