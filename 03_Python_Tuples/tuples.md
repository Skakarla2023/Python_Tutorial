# Python Tuples

- Tuples are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets.

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

Output:
```
('apple', 'banana', 'cherry')
```

![image](https://github.com/user-attachments/assets/fcca8820-65f7-45c8-9b2e-20db7c1f311f)

- A tuple can contain different data types.
- Length of a tuple can be found using len() funtion.
- We can create a tuple with one item.

![image](https://github.com/user-attachments/assets/3d7d6c24-bc31-4614-8874-4e1dd326d1da)

![image](https://github.com/user-attachments/assets/d5c2545d-9c40-4a3b-92c1-38cd41d8ed68)

```python
# basic tuple program
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# a tuple can have data of different types
tuple1=(1,True,"apple")
print(tuple1)

# get the length of the tuple using len() method
mytuple=(1,2,3,4,5)
print(len(mytuple))

# we can also get the datatype of the tuple
tuple2=("a","b","c")
print(type(tuple2))

# we can create a tuple with single element
tup1=("Me")
print(tup1)

# tuples allow duplicates
tup2=("a","b","a","a","c","d")
print(tup2)
```

Output:
```
('apple', 'banana', 'cherry')
(1, True, 'apple')
5
<class 'tuple'>
Me
('a', 'b', 'a', 'a', 'c', 'd')
```

![image](https://github.com/user-attachments/assets/e8943612-06ac-4d8f-949f-84b50cf355b7)

![image](https://github.com/user-attachments/assets/48519c31-880c-4331-8116-979d4539c311)

![image](https://github.com/user-attachments/assets/3d5ead1a-c7eb-4946-8c70-322e6efbdcd3)

![image](https://github.com/user-attachments/assets/f62f371e-2a46-4b69-9f01-bbf51a2f4b39)

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
```

Output:
```
banana
```

![image](https://github.com/user-attachments/assets/c3a683b7-d82a-4c20-8136-dba8a5782682)

![image](https://github.com/user-attachments/assets/21985532-7a69-49f8-96fa-443f51ba2184)

![image](https://github.com/user-attachments/assets/ea8e8838-9a42-4384-bb96-739c067767f1)

![image](https://github.com/user-attachments/assets/2f9247bc-f69d-419e-8836-213fc41db439)

```python
mytuple=("satwika","sandeep","kethana","vaishnavi","Rishi","chaithu")
if "kethana" in mytuple:
    print("yes she exists in my heart")
```

Output:
```
yes she exists in my heart
```

![image](https://github.com/user-attachments/assets/8f756185-b4a6-4a28-b369-fb2a593ffbab)

```python
cars=("BMW","Benz","Hyundai")
x=list(cars)
x[2]="Range Rover"
y=tuple(x)
print(y)
```

Output:
```
('BMW', 'Benz', 'Range Rover')
```

![image](https://github.com/user-attachments/assets/9b3b8d64-e36c-4baf-b6ea-bf36ea5e3f3c)

```java
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
```

Output:
```
('apple', 'banana', 'cherry', 'orange')
```

![image](https://github.com/user-attachments/assets/544602fa-76fa-4db2-8150-e45044140a52)

![image](https://github.com/user-attachments/assets/83c496ad-d3b9-41fd-9fe6-b8e5c63076f3)
