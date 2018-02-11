#!/usr/bin/env python

#replace
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC'))

#slices a string, from the 2nd index (0 is the first) to the 6th, without the 6th
sub = a[1:6]
print(sub)

#prints a string, minus the number of specified characters from the end
mlfb='3SB19012KM-Z'
print(mlfb[:-2])

#prints only the last 2 characters from a string
mlfb='3SB19012KM-Z'
print(mlfb[-2:])

#prints only the first 2 characters from a string
mlfb='3SB19012KM-Z'
print(mlfb[0:2])

#prints a string in reverse....fucking A
hc = 'Horea Nicolae Cotia'
print(hc[::-1])



#split a string into a list of elements
a = "one two three four"
i = a.split()
print(i)


#finding out the length of a string
x=len(a)
print(x)
print(len(a))
