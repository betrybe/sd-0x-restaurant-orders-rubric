from src.track_orders import TrackOrders
import csv


def track_restaurant_orders(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    with open(path_to_file, encoding="utf-8") as file:
        data = list(csv.reader(file))

    tracker = TrackOrders()

    for name, dish, weekday in data:
        tracker.add_new_order(name, dish, weekday)

    return tracker


def analyze_log(path_to_file):
    track = track_restaurant_orders(path_to_file)
    lines = [
        track.get_most_ordered_dish_per_customer("maria"),
        track.get_order_frequency_per_customer("arnaldo", "hamburguer"),
        track.get_never_ordered_per_customer("joao"),
        track.get_days_never_visited_per_customer("joao")
    ]

    with open('data/mkt_campaign.txt', "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")
