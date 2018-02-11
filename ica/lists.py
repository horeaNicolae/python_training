#!/usr/bin/env python

cars = ["BMW", "Mercedes-Benz", "Audi", "Honda", "Nissan"]

length_cars = len(cars)
print(length_cars)

print(cars)

#Append an item to the list => last position
cars.append("Subaru")
print(cars)

#Insert an element to a list, define the index and then the element
cars.insert(1, "Suzuki")
print(cars)

#Finds the index of a particular item from the list
x = cars.index("Honda")
print(x)

#Removes the last item from the list
y = cars.pop()
print(y)
print(cars)

#Removes a specific element from the list
cars.remove("Nissan")
print(cars)

#Slicing an element from the list
slicing = cars[0:2]
print(slicing)

a = cars[1:]
print(a)

#Sort the list
cars.sort()
print(cars)
