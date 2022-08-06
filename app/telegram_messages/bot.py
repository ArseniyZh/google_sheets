import telegram

from config.config import personal_id

_lated_order_set = set()


# https://t.me/test_task_zhelvakov_bot
def send_message(numbers: list) -> None:
    """Sending notifications about lated orders in Telegram."""
    _bot = telegram.Bot('5589810317:AAGnF3zYqryF4IT7Av8uRHy0fTK04QMe9Og')
    _bot.send_message(
        personal_id,
        f'Срок поставки заказа(ов) №{", ".join(map(str, numbers))} истек'
    )


# Checking the freshness of the order
def check_fresh_order(numbers: list) -> None:
    """Allows you to find the numbers of orders that have already been notified"""
    global _lated_order_set

    # Finding new elements in numbers
    _diff = _lated_order_set.difference(numbers)
    for elem in _diff:
        _lated_order_set.remove(elem)

    # The values relative to _lated_order_set can become either more or less
    _var = set(numbers).difference(_lated_order_set) or _lated_order_set.difference(set(numbers))
    _order_set_now = _lated_order_set

    if numbers and _var:
        _lated_order_set = _var
        send_message(sorted(list(_lated_order_set)))
        _lated_order_set = _order_set_now.union(_var)
