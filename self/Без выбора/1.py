import random


def insertion(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


a = [random.randint(1, 1000) for i in range(20)]
print("Исходный массив:", a)
print("Сортировка вставкой:", insertion(a))
print("Сортировка sorted:", sorted(a))
a.sort()
print("Сортировка sort:", a)
