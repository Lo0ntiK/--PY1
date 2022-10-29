def get_count_char(str_):
    dict_chars = {}
    default_val = 0
    for char in str_.lower():
        if char.isalpha():
            dict_chars[char] = dict_chars.get(char,default_val) + 1
    return dict_chars

def percents(dict_chars):
    summ = sum(dict_chars.values())
    new_dict_chars = {}
    for char in dict_chars.keys():
        new_dict_chars[char] = dict_chars.get(char,0)/summ * 100
    return new_dict_chars

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percents(get_count_char(main_str)))
