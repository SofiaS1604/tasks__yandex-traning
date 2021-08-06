a = int(input())
b = int(input())
c = int(input())

if c >= 0 and a != 0:
    if ((c*c - b) / a) - ((c*c - b) // a) > 0:
        print("NO SOLUTION")
    else:
        print((c*c - b) // a)
elif (a == 0 and b == 0 and c == 0) or (a == 0 and b == c ** 2):
    print("MANY SOLUTIONS")
else:
    print("NO SOLUTION")