# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)
    return duplicates
    
def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 3, 2, 4, 3, 5, 6, 5, 7, 8, 9, 7]
duplicates = find_duplicates(lst)
print("Повторяющиеся элементы:", duplicates)

result = remove_duplicates(lst)
print("Итоговый список без повторяющихся элементов:", result)