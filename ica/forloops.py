
#Prints prints the string, replaces a small d with a capital D, counts the occurrences of d

myString = 'abcdefgd'
dcount = 0
for c in myString:
    if c == 'd':
        print ('D', end = ' ')
        dcount+=1
    else:
        print(c, end = ' ')
print("\r\nTotal counts of 'd' string = {} ".format(dcount))


#list for loop
operatingSystems = ['Windows', 'MacOS', 'Linux']
for OS in operatingSystems:
    print(OS)

print('*' * 20)


#numbers for loop
numbers = [1,2,3,4]
for n in numbers:
    print(n * 10)

print('*' * 20)

#dictionary for loop
#by default, this prints the keys
tupi = {'one': 1, 'two': 2, 'three': 3}
for k in tupi:
    print(k)

print('*' * 20)

#this prints the keys & their values
tupi = {'one': 1, 'two': 2, 'three': 3}
for k in tupi:
    print(k + ' ' + str(tupi[k]))

print('*' * 20)

for k,v in tupi.items():
    print(k)
    print(v)
