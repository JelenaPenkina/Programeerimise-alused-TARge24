class Order:
    """Combination of order items of one customer."""

    def __init__(self, order_items: list):
        """
        Order constructor.

        :param order_items: list of order items.
        """
        self.order_items = order_items

    @property
    def total_quantity(self) -> int:
        """
        Calculate and return the sum of quantities of all items in the order.

        :return: Total quantity as int.
        """
        return sum(item.quantity for item in self.order_items)

    @property
    def total_volume(self) -> int:
        """
        Calculate and return the total volume of all items in the order.

        :return: Total volume (cm^3) as int.
        """
        return sum(item.total_volume for item in self.order_items)