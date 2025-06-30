# Python Strings

![image](https://github.com/user-attachments/assets/23709f4b-f4fc-405b-ad5a-7ea7c4ca2c9c)

![image](https://github.com/user-attachments/assets/a9f3d54a-6ec9-40fe-b5d6-cbe403e39133)

```python
x=int(1)    # 1
y=int(1.1)  # 1
z=int("3")  # 3
```

![image](https://github.com/user-attachments/assets/4490e01c-97d1-4a46-84a3-726508c7e28d)

```python
a="welcome"
print(len(a))
print(type(a))
print("o" in a)
print("m" not in a)
```

![image](https://github.com/user-attachments/assets/3f2cb87d-0027-4539-9efe-7fe2df32c7a1)

![image](https://github.com/user-attachments/assets/d4b18ec6-ada4-4afd-abe4-5952b26f6005)

![image](https://github.com/user-attachments/assets/97c963da-7dc3-422a-9838-fff762782afc)

```python
a = "Hello people"
print(a[:5]) 		# outputs from starting till 5th index
print(a[4:])  		# outputs from 4th to last index
print(a[-6:-1]) 	# outputs 6th char from last to first char from last
```

## Python Modify Strings

```python
# Python Modify Strings example
a = "Welcome"


# converts into uppercase
print(a.upper())	

# converts into lowercase
print(a.lower())	

#splits the string into a list of substrings
print(a.split())	

# replaces l with b in the string
print(a.replace("l","b"))	
```

![image](https://github.com/user-attachments/assets/5b1e6e80-68bb-44d5-bbd1-a582d56a0973)

![image](https://github.com/user-attachments/assets/1fc2a7b4-c48d-48b5-b27e-606f5b34f4fc)

```python
a = "Anbe "
b = "sivam"
print(a+b)    # outputs ANbe sivam
```

## Python - Format - Strings

- we can combine strings and numbers by using f-strings or the format() method!
  
![image](https://github.com/user-attachments/assets/29a5a5ea-9fd7-4634-8d20-0e2307ea81f0)

```python
age = 25
txt=f"My name is Paul, I am {age} years old"
print(txt)
```

![image](https://github.com/user-attachments/assets/aa8a4d72-ec00-4e6e-b5b2-a3d97d2b821a)

```python
price = 20
txt = f" Bananas are sold at {price} per dozen"
print(txt)
```

Output:
```
Bananas are sold at 20 per dozen
```

![image](https://github.com/user-attachments/assets/eecd3939-9894-49f3-9096-c9c4018fe297)

```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```

Output:
```
The price is 59.00 dollars
```

![image](https://github.com/user-attachments/assets/9206d39f-0dc4-43a5-8921-408c775a947b)

Output:

```
The price is 1180 dollars
```

![image](https://github.com/user-attachments/assets/f8dc1bff-de09-45dc-beb3-9756dc5af038)

![image](https://github.com/user-attachments/assets/02cd140a-c8ba-4119-b963-0da60729fb17)
