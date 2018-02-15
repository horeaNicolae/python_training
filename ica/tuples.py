#!/usr/bin/env python

#Define a list, just to prove that they are mutable
my_list = [1, 2, 3]
print(my_list)

my_list[0] = 0
print(my_list)

print("This is where we will print tuples")
#Define a tuple
my_tuple = (1, 2, 3, 2, 1, 1, 2, 3)
print(my_tuple)
#my_tuple[0] = 0
#the above statement will return an error: tuple object does not support assignment

print(my_tuple[0])

#We can do slicing & other shit, like with lists
print(my_tuple[1:])

print(my_tuple.index(3))

#This is where we count how many times we have the number 1
print("\n\rThis is where we count how many times we have the number 1 in the tuple")
print(my_tuple.count(1))
