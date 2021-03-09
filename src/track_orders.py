from collections import defaultdict, Counter
from src.order import Order


class TrackOrders:
    def __init__(self):
        self.orders = defaultdict(Order)
        self.all_dishes = Counter()
        self.all_weekdays = Counter()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        print(f"{costumer}  {order}  {day}")
        self.orders[costumer].add(order, day)
        self.all_dishes[order] += 1
        self.all_weekdays[day] += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        return self.orders[costumer].most_common_dish()

    def get_order_frequency_per_costumer(self, costumer, order):
        return self.orders[costumer].dishes[order]

    def get_never_ordered_per_costumer(self, costumer):
        costumer_activity = self.orders[costumer].dishes.keys()
        return self.all_dishes.keys() - costumer_activity

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_activity = self.orders[costumer].weekdays.keys()
        return self.all_weekdays.keys() - costumer_activity

    def get_busiest_day(self):
        return self.all_weekdays.most_common(1)[0][0]

    def get_least_busy_day(self):
        return self.all_weekdays.most_common()[-1][0]
