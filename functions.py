
'''
Write a Python function, add(), that takes two numbers and sums them up.

Example:
>>> add(120,100)
220
>>> add(120,10)
130
'''
#code:
def add(x, y):
    return(x+y)
def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

num_x = input()
num_y = input()

num_x = remove_special_chars(num_x)
num_y = remove_special_chars(num_y)


if(num_x.isdigit() and num_y.isdigit()):
    
    num_x = int(num_x)
    num_y = int(num_y)
    print(add(num_x, num_y))

'''
Write a Python function, subtract, that takes two number and subtract them.


Example:
>>> subtract(120,100)
   20
>>> subtract(120,10)
   110
   '''
#code:


def sub(x, y):
    return(x-y)
def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

num_x = input()
num_y = input()

num_x = remove_special_chars(num_x)
num_y = remove_special_chars(num_y)


if(num_x.isdigit() and num_y.isdigit()):
    
    num_x = int(num_x)
    num_y = int(num_y)
    print(sub(num_x, num_y))


'''
Write a Python function, multiply, that takes two number and multiply them.

Example:
>>> multiply(120,100)      
    12000
>>> multiply(3,4)      
    12
    
'''
#code:
def multiply(x, y):
    return(x*y)
def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

num_x = input()
num_y = input()

num_x = remove_special_chars(num_x)
num_y = remove_special_chars(num_y)


if(num_x.isdigit() and num_y.isdigit()):
    
    num_x = int(num_x)
    num_y = int(num_y)
    print(multiply(num_x, num_y))

'''
Write a Python function, divide( ), that takes two numbers and divide them.

Example:
>>> 
12
10
divide(120,10)
12
>>> 
120
0
divide(120,0)
Division by zero.
'''
#code:
def divide(x, y):
    return(int(x)//int(y))
    
def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

num_x = input()
num_y = input()

num_x = remove_special_chars(num_x)
num_y = remove_special_chars(num_y)


if(num_x.isdigit() and num_y.isdigit()):
    if (int(num_x) != 0 and int(num_y) != 0):
        result = divide(num_x, num_y)
    else:
        result = "Division by zero."
    print(result)

'''
Write a Python function choose, that asks a user to enter two numbers and ask if he/she wants to add(+), multiply(*), subtract(-) or divide(/). (Do use add, subtract, multiply and divide function that you have developed previous problems of this problem set.

Example:

>>> Enter a number: 12
    Enter a number: 13
    What do you want to do: add(+), multiply(*),subtract(-) or divide(/) ? add
    Result is 25.
>>> Enter a number: 10
    Enter a number: 5
    What do you want to do: add(+), multiply(*),subtract(-) or divide(/) ? subtract
    Result is 5.
>>> Enter a number: 56
    Enter a number: 8
    What do you want to do: add(+),multiply(*),subtract(-) or divide(/) ? divide
    Result is 7.
>>> Enter a number: 8
    Enter a number: 10
    What do you want to do: add(+),multiply(*),subtract(-) or divide(/)? multiply
    Result is 80.
'''
#code:

num1 = input()
num2 = input()
action = input()

def remove_special_chars(input):
    return ''.join(e for e in input if e.isalnum())


def convert_to_int(num):
    if num.isdigit():
        return int(num)
    else:
        print("Error! Input is not a number!")

def add(num1, num2):
    return(num1 + num2)

def subtract(num1, num2):
    return(num1 - num2)
    
def multiply(num1, num2):
   return(num1 * num2)
    
def divide(num1, num2):
    return(num1 // num2)   
   
def choose(num1, num2, action):
    result = "Null"
    if(action == "add" or action == "addition"):
        result = add(num1, num2)
    elif(action == "multiply" or action == "multiplication"):
        result = multiply(num1, num2)
    elif(action == "subtract" or action == "subtraction"):
        result = subtract(num1, num2)
    elif(action == "divide" or action == "division"):
        if (int(num1) != 0 and int(num2) != 0):
            result = divide(num1, num2)
        else:
            result = "Division by 0."
    else:
        result = "Error! Action not chosen!"
    return result
    

print("Result is " + str(choose(convert_to_int(remove_special_chars(num1)), convert_to_int(remove_special_chars(num2)), remove_special_chars(action))) + ".")

'''
Write a Python function, square, that takes in one number and returns the square of that number.

def square(x):

        ' ' '

        x: int or float.

        ' ' '

        # your code here

x = int(input())

**After writing a function you must include the inputs at the end of the function, how it is shown above.

Example:
>>>square(4)
   16
>>>square(0)
   0
>>>square(15)
   225
  '''
#code:


x = int(input("Enter a square: "))

def square(x):
    
  return x*x

print(square(x))

'''
Write a Python function that calculates the area of rectangle.


def rectangle_area(width, height):

    ' ' ' num, num -> num

    Returns the area of the rectangle with dimensions:width & height

    >>> rectangle_area(4,5)

    20

    ' ' '

    # your code here

x = int(input())

y = int(input())

**Include inputs at the end of the function as it has shown above.

Example:

>>> rectangle_area(3,4)  
    12 
>>> rectangle_area(3,-4)
    'Incorrect input!' 
>>> rectangle_area(0,4) 
    'Incorrect input!' 
>>> rectangle_area(2,4)
    8
'''
#code:

def rectangle_area(x, y):
    return(int(x)*int(y))
    
def remove_spaces(thisString):
    return (thisString.replace(" ", ""))

num_x = input()
num_y = input()

num_x = remove_spaces(num_x)
num_y = remove_spaces(num_y)

if(num_x.isdigit() and num_y.isdigit()):
    if (int(num_x) <= 0 or int(num_y) <= 0):
        print("Incorrect input!")
    else:
        print(rectangle_area(int(num_x), int(num_y)))
else:
    print("Incorrect input!")

'''
Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if. This function takes in one number and returns a boolean.


def odd(x):

    '''

    x: int or float.

    returns: True if x is odd, False otherwise

    '''

    # Your code here

x = int(input())

**Include input at the end of the program like shown above.

Example:
>>> odd(5)
    True
>>> odd(0)
    False
>>> odd(-9)
    True
>>> odd(14)
    False
'''
#code:
x = int(input())

if (x % 2 != 0):
    print("True")
else:
    print("False")

'''
Write a Python function, numberPower, that takes in two numbers and returns first number raised to the second number power.

You should use the for loop.

Input:

This function takes in two numbers.

Output:
Function returns one number .


def numberPower(x,y):

    ' ' '

    x: int or float.

    y: int.

    ' ' '

    # Your code here

x = int(input())

y = int(input())

**Include inputs at the end of the program like shown above.

Example:

>>> numberPower(5, 3)
    125
>>> numberPower(11,2)
    121
>>> numberPower(1,100)
    1
    
'''