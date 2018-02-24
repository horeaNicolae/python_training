l1 = [1, 2, 9]
l2 = [7, 8, 3, 12, 14, 16]

for a, b in zip(l1, l2):
    if a > b:
        print (a)
    else:
        print (b)

print('*' * 30)

l10 = [12, 14, 21]
l11 = [15, 20, 19]
l12 = [18, 17, 16]

for x, y, z in zip(l10, l11, l12):
    if x > y or x > z:
        print(x)
    elif y > z:
        print(y)
    else:
        print(z)
