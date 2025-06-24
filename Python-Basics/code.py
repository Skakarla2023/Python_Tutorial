# variables in python
a=3
b=4
print(a+b)


# declaring variables

# camel-case
myVar=4
print(myVar)

# snake-case
my_var=5
print(my_var)

# Pascal case
MyVar=4
print(MyVar)


# if in python
if(5>2):
  print("5 is greater than 2")
else:
  print("5 is not greater than 2")


# declaring multiple variables is easy
fruits="apple","banana","cherry"
x,y,z=fruits
print(x)
print(y)
print(z)


# global variables
x="awesome"

def myfunc():
  x="fantastic"
  print("python is",x)

myfunc()
print("python is",x)


# changing the value of global variables

x="awesome"

def myfunc():
  global x
  x="fantastic"
  print("python is",x)

myfunc()
print("python is",x)


# strings in python

s="awesome"
print(s.split())
print(s.strip())
print(s.upper())


