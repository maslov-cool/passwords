import random
import string


big_letters = [i for i in string.ascii_uppercase if i not in 'OI']
small_letters = [i for i in string.ascii_lowercase if i not in 'ol']
digits = [i for i in string.digits if i not in '01']


def generate_password(m):
    global big_letters, small_letters, digits
    password = set(random.choices(big_letters + small_letters + digits, k=m - 3))
    password.add(random.choice(big_letters))
    password.add(random.choice(small_letters))
    password.add(random.choice(digits))
    while len(password) != m:
        password.add(random.choice(big_letters + small_letters + digits))
    return ''.join(password)


def main(n, m):
    set_ = {generate_password(m) for _ in range(n)}
    while len(set_) != n:
        set_.add(random.choice([generate_password(m), ''.join(random.sample(random.choice(list(set_)), m))]))
    return list(set_)

