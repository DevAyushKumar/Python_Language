'''Function argument and return statements:
There are four types of arguments you can provide to a function:
* Default arguments
* Keywords arguments
* Varaible length arguments
* Required variables

Default arguments:
We can provide a defualt value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.'''
def name(fname, mname = "Ayush", lname="kumar"):
    print('Hello', fname, mname, lname)
name("array")

'''Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the order in which the arguments are passed does not matter'''
#example
def name(fname,mname,lname):
    print("hello", fname, mname, lname)
name(mname = "Kumar", lname = "Ritik", fname = "Rishu")

'''Required arguments:
In case we don't pass the arguments with the a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actucal function defination'''
def name1(fname, mname, lname):
    print("Hello", fname, mname, lname)

#name1("Ayush", "Kumar")

'''Variable-length argument:
'''