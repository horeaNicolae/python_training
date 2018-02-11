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

num_list = [1, 2, 1, 3, 4, 1, 5]
print(num_list)

#Counts the number of times that an element can be found in a list
nl_ct = num_list.count(1)
print(nl_ct)

#prints the last two elements from the
print(num_list[-2:])
