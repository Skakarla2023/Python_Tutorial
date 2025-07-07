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

![image](https://github.com/user-attachments/assets/13a0986d-9add-403a-98b1-013e1abcd9f8)

```python
thistuple=("apple","banana","cherry")
y=("kiwi",)
thistuple+=y
print(thistuple)
```

Output:
```
('apple', 'banana', 'cherry', 'kiwi')
```

![image](https://github.com/user-attachments/assets/2c6c94a4-e294-45dc-9ae9-315dd2028be0)

```python
thistuple=("apple","banana","cherry")

#converting tuple to list
y=list(thistuple)

#removing the item from list
y.remove("banana")

#converting the list again to tuple
x=tuple(y)

# print the tuple
print(x)
```

Output:
```
('apple', 'cherry')
```

![image](https://github.com/user-attachments/assets/8e97201a-350c-4909-8a09-0760f428a072)

![image](https://github.com/user-attachments/assets/b367a837-e53a-48ce-a8be-801990da4fde)

```python
life=("me","pride","happiness","family","l")

(a,b,c,d,e)=life

print(a)
print(b)
print(c)
print(d)
print(e)
```

![image](https://github.com/user-attachments/assets/2aa58b96-3624-42ff-b7f5-0756c8c4454b)

![image](https://github.com/user-attachments/assets/c605e40c-a8e2-4e93-b18d-d2e7d4f7421c)

```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
```

Output:
```

apple
banana
['cherry', 'strawberry', 'raspberry']
```

![image](https://github.com/user-attachments/assets/2c00e99f-d094-4076-9727-af0faff3186e)

```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
```

Output:
```

apple
['mango', 'papaya', 'pineapple']
cherry
```

### Python - Loop Tuples

![image](https://github.com/user-attachments/assets/279c8a36-5ec9-41c7-97d9-518bb5a9ea05)

```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

for i in fruits:
	print(i)
```

Output:
```
apple
mango
papaya
pineapple
cherry
```

![image](https://github.com/user-attachments/assets/6459c5e4-109b-4d4b-b8dc-c4ec0625239b)

```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

for i in range(len(fruits)):
	print(fruits[i])
```

![image](https://github.com/user-attachments/assets/49768243-b9a4-493f-b7c3-3b1eda760a29)

```python
 mytuple=("a","b","c")
i=0

while i < len(mytuple):
  print(mytuple[i])
  i = i + 1
```

Output:
```
a
b
c
```

![image](https://github.com/user-attachments/assets/b1470957-1c25-4ebb-8535-c078e0e1e466)

```python
tuple1 = ("A","B","C","D")
tuple2 = ("E","F","G","H")

tuple3 = tuple1 + tuple2
print(tuple3)
```

Output:
```
('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
```

![image](https://github.com/user-attachments/assets/4af789ce-257e-4e73-98a8-dd2b39fc56b1)

```python
tuple1 = ("A","B","C","D")
tuple2 = ("E","F","G","H")

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple3*3
print(tuple4)
```

Output:
```
('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
```

![image](https://github.com/user-attachments/assets/dfc83626-955c-419b-87ad-49daa4f1bbe1)

```python
tuple1=("A","B","C","D",1,2,3,4)
print(tuple1.count("B"))
print(tuple1.index(3))
```

Output:
```
1
6
```
