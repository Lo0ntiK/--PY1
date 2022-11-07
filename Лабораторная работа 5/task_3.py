from random import randint, shuffle


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(set(list_)) != 15:
        list_.append(randint(-10,10))
    list_ = list(set(list_))
    shuffle(list_)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

