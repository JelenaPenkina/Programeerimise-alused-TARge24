import Container

class ContainerAggregator:
    """Algorithm to prepare containers."""

    def __init__(self, container_volume: int):
        """
        Initialize Container Aggregator.

        :param container_volume: Volume of each container created by this aggregator.
        """
        self.container_volume = container_volume
        self.containers = []

    def prepare_containers(self, orders: tuple) -> dict:
        """
        Create containers and put orders to them.

        If order cannot be put to a container, it is added to self.not_used_orders list.

        :param orders: tuple of orders.
        :return: dict where keys are destinations and values are containers to that destination with orders.
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


