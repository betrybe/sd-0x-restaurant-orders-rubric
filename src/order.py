from collections import Counter


class Order:
    def __init__(self):
        self.dishes = Counter()
        self.weekdays = Counter()

    def add(self, dish, weekday):
        self.dishes[dish] += 1
        self.weekdays[weekday] += 1

    def most_common_dish(self):
        return self.dishes.most_common(1)[0][0]
