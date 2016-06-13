# Function that computes the area of a triangle.  
# Header: the definition of a fuction with the word def.
# The : means a new block of code is going to start. 
# The indentation of the code after the colomn is the body code of the fuction. 

def triangle_area(base, height): #header of the function.
#Body of the fuction. 

    area = (1.0 / 2) * base * height
    return area # Returs tells Python the output of the fuction. 

## Fucntion call 
a1 = triangle_area(3, 8)
print a1

a2 = triangle_area(14, 2)
print a2

# converst fahrenheit to celsius. 
def fa2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

## Call 
c1 = fa2celsius(32)
c2 = fa2celsius(212)
print c1, c2

# Converts fahrenheit to kelvin. 
def fa2kelvin(fahrenheit):
    celsius = fa2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

## Call 
k1 = fa2kelvin(32)
k2 = fa2kelvin(212)
print k1, k2

# Prints "Hello World!"
def hello():
    print "Hello world!"
    
# Test 
hello()
h = hello()
print h