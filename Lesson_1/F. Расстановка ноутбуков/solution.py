# coding=utf-8
"""
    Вводим 4 числа: длину и ширину 1 ноутбука, длину и ширину 2 ноутбука. Вводим комбинации, которые могут быть.
    Из них выбираем 2 минимальных произведения.
"""


a1, b1, a2, b2 = map(int, input().split())

combinations = [
        (a1 + a2, max(b1, b2)),
        (a1 + b2, max(b1, a2)),
        (max(a1, a2), b1 + b2),
        (max(a1, b2), b1 + a2)
    ]

result = min(combinations, key=lambda y: y[0] * y[1])
print(result[0], result[1])
