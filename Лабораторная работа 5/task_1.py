from pprint import pprint


def dict_f(number: int) -> dict:
    dict_ = {
        'bin': bin(number),
        'oct': oct(number),
        'dec': number,
        'hex': hex(number)
    }
    return dict_


list_ = [dict_f(i) for i in range(16)]
pprint(list_)

