#!/usr/bin/env python

car = {'make': 'Honda', 'model': 'Civic', 'year': 2004}
print(car)

#define an empty dictionary, to add items to it later
a = {}

model = car['model']
print(car['make'])
print(model)

#add items to the empty dictionary
a['one'] = 1
a['two'] = 2

print(a)

#putem manipula valorile din lista
suma_1 = a['two'] + 8
print(suma_1)

print(a)

#putem schimba valoarile din lista
a['two'] = a['two'] + 18
print(a)


#NESTED DICTIONARIES

print("\n\rThis is where NESTED DICTIONARIES begin")
n_cars = {'Honda': {'model': 'Civic', 'year': 2006}, 'Nissan': {'model': 'Patrol', 'year': 2004}}

#this will print the entire nested dictionary of Honda
print(n_cars['Honda'])

#this will print just the year of the Honda, but it does so by using a variable
honda_year = n_cars['Honda']['year']
print(honda_year)

#this does the same as above, but without using a variable
print(n_cars['Nissan']['year'])





#DICTIONARY METHODS
print("\n\rThis is where DICTIONARY METHODS begin")
#prints the keys of the dictionary
print(car.keys())
print(n_cars.keys())

print('\n\r')

#prints the values of the dictionary
print(car.values())
print(n_cars.values())

#prints the items inside the dictionaries
print('\n\r')
print(car.items())
print(n_cars.items())

#copy a DICTIONARY
print('\n\r')
nested_cars_copy = n_cars.copy()
print('This is the copy of the nested cars dictionary:')
print(nested_cars_copy)


#clear a DICTIONARY
#car.clear()

#removes the key 'model' from the dictionary.
print("This is where we remove the model, and then print what remains the in car dictionary")
print(car.pop('model'))
print(car)
