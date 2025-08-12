# 🍁 Python Functions

- Function is a container that contains some lines of code.
- There are several in-built functions in python which have their own purpose and perform their function such as:
  - input() - used to take input from the user
  - print() - used to print a statement

  #### 🎖️ Rules for writing a funtion:

1. Always declare the funtion using **def** keyword.
2. The def keyword should be followed by the function name.
3. Function name should always be in lowercase letters.
4. If there are multiple words in a function name seperate them by using **_**(an underscore).
5. It is always suggested to use meaningful,easy and understandable names for functions.

The following is an example for a simple function:

```python
def greet_user():
    print("Hi there!")
    print("Welcome aboard!")


print("Start")
greet_user()
print("Finish")
```

Output:
```
Start
Hi there!
Welcome aboard!
Finish
```

- One should always call a function after defining it, otherwise it would throw an error.

### Function Parameters:

- In functions arguments and function parameters are different, the actual values that we pass into the function are called arguments.
- Parameters are the variables inside a function used to receive the values that we passed into a function

- You can pass as many parameters that you want in a function.
- see the following basic code for passing arguments into a function:

```python
def greet_user(first_name,last_name):
    print("Hi "+first_name+" "+last_name)
    print("Welcome to India")


print("Good morning everyone")
greet_user("Lalitha","Kumari")
greet_user("Mary","John")
print("See y'all")
```

Output:
```
Good morning everyone
Hi Lalitha Kumari
Welcome to India
Hi Mary John
Welcome to India
See y'all
```

#### Positional Arguments:

- These are the arguments that are passed into the function based on their value in the function call.
- The order of arguments inside the function should be same as the order of functions in the function call, otherwise it would throw an error.

observe the following piece of python code for better understanding:

```python
def details(name,age):
    print("Hi, I am "+name)
    print("I am "+age+" years old")


details(24,"Saritha")
```

Output:

<img width="1402" height="727" alt="image" src="https://github.com/user-attachments/assets/6439fed7-b497-4f21-8af1-a98ab659c618" />


```python
def details(name,age):
    print("Hi, I am "+name)
    print("I am ",age," years old")


details("Saritha",24)
```

Output:
```
Hi, I am Saritha
I am  24  years old
```

### Keyword Arguments

- These parameters are identified by their parameter names in the function call, and they can be in any order.

```python
def details(name,age):
    print("Hi, I am "+name)
    print("I am ",age," years old")


details(age=24,name="Saritha")
```

Output:
```
Hi, I am Saritha
I am  24  years old
```

