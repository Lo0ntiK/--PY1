list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]
pos_max=0
for i in range(len(list_numbers)):
    if list_numbers[i] > max_number:
        max_number = list_numbers[i]
        pos_max = i
list_numbers[pos_max], list_numbers[-1] = list_numbers[-1], list_numbers[pos_max]

print(list_numbers)

