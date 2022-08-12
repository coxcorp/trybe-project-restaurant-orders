from collections import Counter


class TrackOrders:
    def __init__(self):
        self._data = list()
        self._menu = set()
        self._days = set()

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append({"customer": customer, "order": order, "day": day})
        self._menu.add(order)
        self._days.add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        result = list()
        for order in self._data:
            if customer in order["customer"]:
                result.append(order["order"])
        return Counter(result).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        result = list()
        for order in self._data:
            if customer in order["customer"]:
                result.append(order["order"])
        return self._menu.difference(result)

    def get_days_never_visited_per_customer(self, customer):
        result = list()
        for order in self._data:
            if customer in order["customer"]:
                result.append(order["day"])
        return self._days.difference(result)

    def get_busiest_day(self):
        result = list()
        for order in self._data:
            result.append(order["day"])

        return Counter(result).most_common(1)[0][0]

    def get_least_busy_day(self):
        result = list()
        for order in self._data:
            result.append(order["day"])

        return Counter(result).most_common()[-1][0]
