number = input()
clear_number = number.replace('+', '').replace(' ', '').replace\
    ('-', '').replace('(', '').replace(')', '')

print(clear_number)