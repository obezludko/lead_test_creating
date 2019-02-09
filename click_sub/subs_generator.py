import random

"""This script generate pseudo random subs,
   that will be used in click get request
"""


def generate_sub1():
    random_int = random.randint(1, 9999999)
    random_str = str(random_int) + ' sub 1 ' + str(random_int)
    sub1 = random_str
    return sub1

def generate_sub2():
    random_int = random.randint(1, 9999999)
    random_str = str(random_int) + ' sub 2 ' + str(random_int)
    sub2 = random_str
    return sub2

def generate_sub3():
    random_int = random.randint(1, 9999999)
    random_str = str(random_int) + ' sub 3 ' + str(random_int)
    sub3 = random_str
    return sub3

def generate_sub4():
    random_int = random.randint(1, 9999999)
    random_str = str(random_int) + ' sub 4 ' + str(random_int)
    sub4 = random_str
    return sub4

def generate_sub5():
    random_int = random.randint(1, 9999999)
    random_str = str(random_int) + ' sub 5 ' + str(random_int)
    sub5 = random_str
    return sub5


