def get_count_char(str_):
    dict_chars = {}
    default_val = 0
    char_list = list(str_.lower())
    for char in char_list:
        if char.isalpha():
            dict_chars[char] = dict_chars.get(char,default_val) + 1
    return dict_chars

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

