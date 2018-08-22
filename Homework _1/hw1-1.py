# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

import functools as ft
import operator as op


# --------------------------------------

def calc_sum_v1(number):
    return ft.reduce((lambda x, y: int(x) + int(y)), str(number))


def calc_sum_v2(number):
    return sum([int(i) for i in str(number)])
    # return ft.reduce(op.add, [int(i) for i in str(number)])


def calc_sum_v3(number):
    digits = [int(i) for i in str(number)]
    sum_of_digits = 0
    for d in digits:
        sum_of_digits += d
    return sum_of_digits


def calc_sum_v4(number):
    return 0
#     r1 = (lambda array: (
#             z = 0,
#             for d in array:
#             z += d
#             z))
# lambda array: (
#     result = 0
#
# )
# TODO: use lambda with for loop if possible


# --------------------------------------

def calc_prd_v1(number):
    return ft.reduce((lambda x, y: int(x) * int(y)), str(number))


def calc_prd_v2(number):
    return ft.reduce(op.mul, [int(i) for i in str(number)])


def calc_prd_v3(number):
    digits = [int(i) for i in str(number)]
    prod_of_digits = 1
    for d in digits:
        prod_of_digits *= d
    return prod_of_digits


# Вынос способов решения в отдельные функции в нескольких вариантах
calc_sum = calc_sum_v3
calc_prd = calc_prd_v3

while True:
    try:
        n = int(input('Введите трёхзначное число (или просто Enter для выхода): '))
    except ValueError:
        break
    if (n >= 100) and (n < 1000):
        my_sum = calc_sum(n)
        print(f" Cумма разрядов: {my_sum}")
        my_prd = calc_prd(n)
        print(f" Произведение разрядов: {my_prd}")
        break
    else:
        print('- Вы ввели неверное число')
