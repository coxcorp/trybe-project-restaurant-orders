import csv
from src.track_orders import TrackOrders


def read_file(path_to_file):
    with open(path_to_file, "r") as raw:
        return [row for row in csv.reader(raw)]


def create_data(orders):
    track_orders = TrackOrders()
    for customer, order, day in orders:
        track_orders.add_new_order(customer, order, day)
    return track_orders


def analyze_report(orders):
    track_orders = create_data(orders)
    maria_eats = track_orders.get_most_ordered_dish_per_customer("maria")
    arnaldo_ask_hamburguer = track_orders.asked_by_customer(
        "arnaldo", "hamburguer"
    )
    joao_never_ask = track_orders.get_never_ordered_per_customer("joao")
    joao_never_went = track_orders.get_days_never_visited_per_customer("joao")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{maria_eats}\n"
            f"{arnaldo_ask_hamburguer}\n"
            f"{joao_never_ask}\n"
            f"{joao_never_went}\n"
        )


def analyze_log(path_to_file):
    if not (".csv") in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        orders = read_file(path_to_file)
        analyze_report(orders)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
