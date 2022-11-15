from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n: int = 8) -> str:
    str_ = ascii_uppercase + ascii_lowercase + digits
    password = "".join(sample(str_,n))
    return password


print(get_random_password())

