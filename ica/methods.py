#with this method, position matters. Te first number used when calling the method (e.g. 12, 33)
#will be assigned to n1. The second one, to n2.

def div_nums(n1, n2):
    print(n1 / n2)


div_nums(12, 4)
div_nums(33, 3)

print('*' * 40)


#this method uses optional parameters. If none are provided when calling the method, it has
#default values
def div_nums_optPar(n1 = 4, n2 = 2):
    return n1 / n2

#because if has a fallback, you can give all, some, or none of the parameters when calling the method
o = div_nums_optPar()

v = div_nums_optPar(n2=7, n1 = 35)

p = div_nums_optPar(n2 = 4)

print(o)
print(v)
print(p)


print('*' * 40)

#few examples with built in methods
l = ['a', 'b', 'c']
l.reverse()
print(l)

n = [1, 2, 3]
n.reverse()
print(n)

print(len(l))


print('*' * 40)



#checks if the city is a metro, prints a message whether true or  false
def isMetro(city):
    l = ['San Francisco', 'New York City', 'Los Angeles']

    if city in l:
        return True
    else:
        return False

x = isMetro('New York City')
if x == True:
    print('It so is')
else:
    print('Is not')
