from random import randint, shuffle


def get_unique_list_numbers() -> list[int]:
    list_ = []
    for _ in range(15):
        while True:
            number = randint(-10,10)
            if not number in list_:
                list_.append(number)
                break
            else:
                continue
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

