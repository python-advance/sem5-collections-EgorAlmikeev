import random


def list_splitter(l: list, func):
    """
    :param l: list to split
    :param func: how to split
    :return: list_a, list_b
    """
    list_a = []
    list_b = []

    for i in l:
        if func(i):
            list_a.append(i)
        else:
            list_b.append(i)

    return list_a, list_b


a = [random.randint(1, 1000) for i in range(20)]
print("Исходный список:", a)
a, b = list_splitter(a, lambda i: i % 2 == 0)
print("Чётные элементы:", a)
print("Нечётные элементы:", b)
