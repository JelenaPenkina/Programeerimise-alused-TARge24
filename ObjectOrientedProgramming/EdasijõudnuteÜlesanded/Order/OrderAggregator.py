import OrderItem
import Order

class OrderAggregator:
    """Algorithm of aggregating orders."""

    def __init__(self):
        """Initialize order aggregator."""
        self.order_items = []

    def add_item(self, item: OrderItem):
        """
        Add order item to the aggregator.

        :param item: Item to add.
        :return: None
        """
        self.order_items.append(item)

    def aggregate_order(self, customer: str, max_items_quantity: int, max_volume: int):
        """
        Create an order for customer which contains order lines added by add_item method.

        Iterate over added orders items and add them to order if they are for given customer
        and can fit to the order.

        :param customer: Customer's name to create an order for.
        :param max_items_quantity: Maximum amount on items in order.
        :param max_volume: Maximum volume of order. All items volumes must not exceed this value.
        :return: Order.
        """
        items = []
        # collect items to the order here
        total_quantity = 0
        total_volume = 0

        for item in self.order_items[:]:
            if item.customer == customer:
                if total_quantity + item.quantity <= max_items_quantity and total_volume + item.total_volume <= max_volume:
                    items.append(item)
                    total_quantity += item.quantity
                    total_volume += item.total_volume
                    self.order_items.remove(item)

        return Order(items)