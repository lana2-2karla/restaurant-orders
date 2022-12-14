from collections import Counter

from src.analyze_log import (
    days_never_visited,
    dishes_never_ordered,
    most_requested_dish,
)


class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        order = {"name": customer, "dish": order, "order_day": day}
        self.orders.append(order)

    def get_most_ordered_dish_per_customer(self, customer):
        return most_requested_dish(customer, self.orders)

    def get_never_ordered_per_customer(self, customer):
        return dishes_never_ordered(customer, self.orders)

    def get_days_never_visited_per_customer(self, customer):
        return days_never_visited(customer, self.orders)

    def get_busiest_day(self):
        days = []

        for costumer in self.orders:
            days.append(costumer['order_day'])

        counter_days = Counter(days)
        return max(counter_days, key=counter_days.get)

    def get_least_busy_day(self):

        days = []

        for costumer in self.orders:
            days.append(costumer['order_day'])

        counter_days = Counter(days)
        return min(counter_days, key=counter_days.get)
