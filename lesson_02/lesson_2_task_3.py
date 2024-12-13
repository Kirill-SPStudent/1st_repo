from math import ceil


def square(x):
    sq = x ** 2
    return sq


x = float(input("Введите сторону квадрата : "))
res = square(x)
rounded_res = ceil(res)
print(f'Площадь квадрата : {rounded_res}')
