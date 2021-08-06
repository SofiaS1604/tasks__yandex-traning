# coding=utf-8
"""
    Вводятся 5 чисел (a, b, c - размер кирпича; d, e - размер отверстия). Сортируем в массиве числа и сравниваем первые
    и ворые числа, если значения отверстия больше или равно чем кирпича, то выводим "YES", иначе "NO".
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
brick = sorted([a, b, c])
hole = sorted([d, e])

if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print("YES")
else:
    print("NO")