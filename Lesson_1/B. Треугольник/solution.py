# coding=utf-8
"""
    Применяется формула неравенства сторон в треугольнике для всех сторон. Если условие выполняется, то выводим "YES",
    иначе "NO".
"""

a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (c + b > a) and (a + c > b):
    print("YES")
else:
    print("NO")
