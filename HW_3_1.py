# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends = {
  'Paul': ('fork', 'spoon', 'cup'),
  'Tom': ('plate', 'cup', 'blanket'),
  'Bill': ('cup', 'coffee', 'tea')
}

# Какие вещи взяли все три друга
common_items = set(friends['Paul']).intersection(friends['Tom'], friends['Bill'])
print("Вещи, которые взяли все три друга:", common_items)

# Какие вещи уникальны, есть только у одного друга
unique_items = {}
for name, items in friends.items():
    unique_items[name] = set(items).difference(common_items)
print("Уникальные вещи, есть только у одного друга:", unique_items)

# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
for friend, items in friends.items():
  missing_items = set()
  for other_friend, other_items in friends.items():
    if friend != other_friend:
      missing_items = missing_items.union(set(other_items).difference(items))
  if missing_items:
    print("У друга", friend, "отсутствуют вещи:", missing_items)