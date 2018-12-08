
def get_arrays(count: int):
    i = 1
    arrays = []
    while i <= count:
        a = input("Введите множество " + str(i) + " поэлементно через запятую: ")
        a = a.split(",")
        for j in range(len(a)):
            a[j] = int(a[j])

        arrays.append(a)
        i += 1
    return arrays


def calculate(operation_id: int, arrays: list):
    result = set(arrays[0])
    for i in range(1, len(arrays)):
        if operation_id == 1:
            result |= set(arrays[i])
        elif operation_id == 2:
            result &= set(arrays[i])
        elif operation_id == 3:
            result -= set(arrays[i])
    return result


if __name__ == "__main__":

    operations = """
    1. Объединение
    2. Пересечение
    3. Разность
    """

    arrays = get_arrays(int(input("Введите колличество множеств: ")))
    print(operations)
    operation_id = int(input("Введите номер операции: "))
    print("Ответ:", calculate(operation_id, arrays))
