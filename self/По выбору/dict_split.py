# 2 задание: разделение словаря на 2 разных с условием через лямбду

from typing import Callable


def dict_splitter(dict_to_split: dict, sort_function: Callable):
    """
    :param dict_to_split: what to split
    :param sort_function: how to split function
    :return: dict_a, dict_b
    """

    dict_a = {}
    dict_b = {}

    for item in dict_to_split.items():
        if sort_function(item):
            dict_a.update({item[0]: item[1]})
        else:
            dict_b.update({item[0]: item[1]})

    return dict_a, dict_b


if __name__ == '__main__':
    guests = {
        "Guest1": {"Name": "Kenny", "Sex": "male"},
        "Guest2": {"Name": "Eric", "Sex": "male"},
        "Guest3": {"Name": "Bill", "Sex": "male"},
        "Guest4": {"Name": "Angela", "Sex": "female"},
        "Guest5": {"Name": "Pitt", "Sex": "male"},
        "Guest6": {"Name": "Sasha", "Sex": "female"},
        "Guest7": {"Name": "Anna", "Sex": "female"},
        "Guest8": {"Name": "Daria", "Sex": "female"}
    }

    males, females = dict_splitter(guests, lambda item: item[1]["Sex"] == "male")

    print("Male guests:")
    for i in males.items():
        print(i[1]["Name"])
    print()
    print("Female guests:")
    for i in females.items():
        print(i[1]["Name"])
