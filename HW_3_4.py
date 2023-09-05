# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def backpack(max_weight):
    items = {
        'Палатка': 3,
        'Спальный мешок': 2,
        'Термос': 1,
        'Продукты': 1,
        'Кружка': 0.2,
        'Котелок': 1.5,
        'Фонарь': 0.15,
        'Газовый баллон': 4
    }

    backpack_items = {}
    total_weight = 0

    for item, weight in items.items():
        if total_weight + weight <= max_weight:
            backpack_items[item] = weight
            total_weight += weight

    return backpack_items

max_weight = 10
result = backpack(max_weight)

print("Вещи, которые поместятся в рюкзак (итоговая сумма массы не должна превышать", max_weight, "кг):")
for item, weight in result.items():
    print(item, "-", weight, "кг")