from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

def generate_password(length):
    upper_case = [i for i in ascii_uppercase if i not in 'IO']
    lower_case = [i for i in ascii_lowercase if i not in 'lo']
    digit = [i for i in digits if i not in '0']
    chars = upper_case + lower_case + digit

    result = [choice(i) for i in (upper_case, lower_case, digit)]
    result += [choice(chars) for i in range(length-3)]
    return ''.join(result)

def generate_passwords(count, lenght):
    return [generate_password(lenght) for i in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')