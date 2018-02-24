#zip iterates through multiple lists, but stops when the last item of a list is reached.
#e.g. it will stop after processing the 3rd element of the first list. no further elements
#from the second list will be processed either
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
