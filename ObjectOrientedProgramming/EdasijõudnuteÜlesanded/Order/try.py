from typing import List


class OrderItem:
    """Order Item requested by a customer."""

    def __init__(self, customer: str, name: str, quantity: int, one_item_volume: int):
        """
        Order item constructor.

        :param customer: requester name.
        :param name: the name of the item.
        :param quantity: quantity that shows how many such items customer needs.
        :param one_item_volume: the volume of one item.
        """
        self.customer = customer
        self.name = name
        self.quantity = quantity
        self.one_item_volume = one_item_volume

    @property
    def total_volume(self) -> int:
        """
        Calculate and return total volume of all order items together.

        :return: Total volume (cm^3), int.
        """
        return self.quantity * self.one_item_volume


class Order:
    """Combination of order items of one customer."""

    def __init__(self, order_items: List[OrderItem]):
        """
        Order constructor.

        :param order_items: list of order items.
        """
        self.order_items = order_items
        self.destination = None

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


class Container:
    """Container to transport orders."""

    def __init__(self, volume: int):
        """
        Initialize container.

        :param volume: Total volume of the container.
        """
        self.volume = volume
        self.orders = []

    @property
    def volume_left(self) -> int:
        """Calculate remaining volume in the container."""
        return self.volume - sum(order.total_volume for order in self.orders)

    def add_order(self, order: Order) -> bool:
        """
        Add an order to the container if it fits.

        :param order: Order to add.
        :return: True if added, False otherwise.
        """
        if order.total_volume <= self.volume_left:
            self.orders.append(order)
            return True
        return False


class OrderAggregator:
    """Algorithm of aggregating orders."""

    def __init__(self):
        """Initialize order aggregator."""
        self.order_items = []

    def add_item(self, item: OrderItem):
        """
        Add order item to the aggregator.

        :param item: Item to add.
        """
        self.order_items.append(item)

    def aggregate_order(self, customer: str, max_items_quantity: int, max_volume: int) -> Order:
        """
        Create an order for customer which contains order lines added by add_item method.
        """
        items = []
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


class ContainerAggregator:
    """Algorithm to prepare containers."""

    def __init__(self, container_volume: int):
        """
        Initialize Container Aggregator.
        """
        self.container_volume = container_volume
        self.not_used_orders = []

    def prepare_containers(self, orders: tuple) -> dict:
        """
        Create containers and put orders to them.
        """
        containers_by_destination = {}

        for order in orders:
            if order.total_volume > self.container_volume:
                self.not_used_orders.append(order)
                continue

            if order.destination not in containers_by_destination:
                containers_by_destination[order.destination] = [Container(self.container_volume)]

            for container in containers_by_destination[order.destination]:
                if container.add_order(order):
                    break
            else:
                new_container = Container(self.container_volume)
                new_container.add_order(order)
                containers_by_destination[order.destination].append(new_container)

        return containers_by_destination
