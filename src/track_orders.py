from collections import defaultdict, Counter
from src.order import Order


class TrackOrders:
    def __init__(self):
        self.orders = defaultdict(Order)
        self.all_dishes = Counter()
        self.all_weekdays = Counter()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders[customer].add(order, day)
        self.all_dishes[order] += 1
        self.all_weekdays[day] += 1

    def get_most_ordered_dish_per_customer(self, customer):
        return self.orders[customer].most_common_dish()

    def get_order_frequency_per_customer(self, customer, order):
        return self.orders[customer].dishes[order]

    def get_never_ordered_per_customer(self, customer):
        customer_activity = self.orders[customer].dishes.keys()
        return self.all_dishes.keys() - customer_activity

    def get_days_never_visited_per_customer(self, customer):
        customer_activity = self.orders[customer].weekdays.keys()
        return self.all_weekdays.keys() - customer_activity

    def get_busiest_day(self):
        return self.all_weekdays.most_common(1)[0][0]

    def get_least_busy_day(self):
        return self.all_weekdays.most_common()[-1][0]
