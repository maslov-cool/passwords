import string
import random


def generate_password(m):
    return ''.join([random.choice(''.join(i for i in string.ascii_letters.upper() if i not in 'IO') +
                                  ''.join(i for i in string.ascii_letters.lower() if i not in 'lo')
                                  + ''.join(i for i in string.digits if i not in '10'))
                    for _ in range(m)])


def main(n, m):
    set_ = set()
    while len(set_) != n:
        set_.add(generate_password(m))
    return set_
print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")