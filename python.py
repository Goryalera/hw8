class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    # Сортируем по удельной стоимости по убыванию
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0
    taken_items = []

    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:
            # Берем весь предмет
            taken_items.append((item.weight, item.value))
            capacity -= item.weight
            total_value += item.value
        else:
            # Берем часть предмета
            fraction = capacity / item.weight
            value_fraction = item.value * fraction
            taken_items.append((capacity, value_fraction))
            total_value += value_fraction
            capacity = 0  # рюкзак заполнен

    return total_value, taken_items


# Входные данные
items = [Item(2, 10), Item(3, 20), Item(4, 15), Item(5, 25)]
capacity = 8

max_value, chosen = fractional_knapsack(items, capacity)
print(f"Максимальная стоимость: {max_value}")
print("Выбранные предметы (вес, стоимость):")
for weight, value in chosen:
    print(f"Вес: {weight}, Стоимость: {value}")
