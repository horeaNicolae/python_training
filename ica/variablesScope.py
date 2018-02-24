
#Code where we use a method that uses a parameter.
#this parameter is also defined earlier in the code as a variable
#the idea is to see that even though we afftect the varialbe inside the method, it does
#not change the value of the variable, when we use it again outside the method

a = 10

def test_method(a):
    print("Value of local 'a' is: " + str(a))
    a = 2
    print("New value of local 'a' is: " + str(a))

print("Value of global 'a' is: " + str(a))
test_method(a)
print("Did the value of global 'a' change? " +str(a))

print('*' * 40)

#Here we don't pass any parameters to the method.
#However, we define the variable a as global inside the method.
#This way, we can change the global value of the parameter from inside the method


a = 10

def test_method():

    global a

    print("Value of 'a' inside the method is: " + str(a))
    a = 2
    print("New value of 'a' inside the method is changed to: " + str(a))

print("Value of global a is: " + str(a))
test_method()
print("Did the value of global 'a' change? " +str(a))
