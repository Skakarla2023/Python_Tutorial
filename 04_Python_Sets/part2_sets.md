![image](https://github.com/user-attachments/assets/4a5d1294-0ddc-4e9f-b311-4a58c1d0b4b9)

```python
myset={"a","b","c","d"}

for i in myset:
	print(i)
```

Output:
```
d
b
a
c
```

![image](https://github.com/user-attachments/assets/d90a9305-7367-462b-a5ba-2ae5dfc9b1ab)

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# using the union method
print("using the union method:")
set3 = set1.union(set2)
print(set3)

print("\n")

#using the update method
set4={"d","e","f"}
print("using the update method:")
set2.update(set4)
print(set2)

print("\n")

#using the intersect method
s1={1,2,3}
s2={3,4,5}
print("using the intersect method:")
print(s1.intersection(s2))

print("\n")

# using the difference method:
s3={"a","b","c","d"}
s4={"c","d","e","f"}
print("Using the difference method:")
print(s3.difference(s4))

print("\n")

#using symmetric difference method
print("using symmetric difference method:")
s5=s3.symmetric_difference(s4)
print(s5)
```

Output:
```
using the union method:
{1, 2, 3, 'a', 'c', 'b'}


using the update method:
{1, 2, 3, 'd', 'f', 'e'}


using the intersect method:
{3}


Using the difference method:
{'b', 'a'}


using symmetric difference method:
{'e', 'f', 'a', 'b'}
```

- You can use | instead of union  operator
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
```

Output:
```
{3, 'a', 2, 1, 'b', 'c'}
```

![image](https://github.com/user-attachments/assets/e57a83bb-1ddc-4554-9097-47d05542d87a)

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
```

Output:
```
{'c', 'b', 1, Elena, banana, 3, cherry, 'a', apple, John, 2}
```

![image](https://github.com/user-attachments/assets/b881ad51-8d44-4e1e-b51f-aa0a8a4a8a7c)

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
```

Output:
```
{'c', banana, John, Elena, 3, 'a', apple, 2, 1, 'b', cherry}
```

![image](https://github.com/user-attachments/assets/0e235097-4276-437b-86f5-597c1c60cd75)

```python
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

a=[4,5,6]
b={7,8,9}
c=b.union(a)
print(c)
```

Output:
```
{1, 2, 3, 'c', 'b', 'a'}
{4, 5, 6, 7, 8, 9}
```

![image](https://github.com/user-attachments/assets/cc403a6e-6c92-45a5-a51c-214e5c34a79b)

![image](https://github.com/user-attachments/assets/c35a9259-1a94-4e0f-ad4e-9d76ca5f57c6)

![image](https://github.com/user-attachments/assets/20e33863-ed92-4ec0-99ec-c73c323ffb77)

![image](https://github.com/user-attachments/assets/5b6361b2-0efd-4327-9398-c7f8e0d6caf0)

```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
```

output:
```
{'apple'}
```

![image](https://github.com/user-attachments/assets/793db248-0aa0-486c-85aa-1024d7577972)

![image](https://github.com/user-attachments/assets/5c2bcfd6-242e-43f2-89eb-8add3f5df58c)

![image](https://github.com/user-attachments/assets/698e51e1-549d-4718-a8df-b9ea9b0bbb03)

```python
set1 = {"apple", 1, "banana", 0, "cherry",1}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)
```

Output:
```
{False, True, 'apple'}
```

![image](https://github.com/user-attachments/assets/4df357eb-80e9-4c25-bcda-733dc2ec97b7)

```python
set1 = {"apple", "banana" , "cherry","kiwi"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
```

Output:
```
{'cherry', 'kiwi', 'banana'}
```

![image](https://github.com/user-attachments/assets/74025ac2-cf12-414a-864e-a49112695dc4)

```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)
```

Output:
```
{'banana', 'cherry'}
```

![image](https://github.com/user-attachments/assets/649b0879-d398-4965-8bc7-4476087bbc75)

```python
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)
```

Output:
```
{'google', 'banana', 'microsoft', 'cherry'}
```

![image](https://github.com/user-attachments/assets/8c419cf9-9cd8-47a7-8a34-27f15748749c)

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)
```

Output:
```
{'google', 'banana', 'microsoft', 'cherry'}
```

![image](https://github.com/user-attachments/assets/3acad5eb-5bef-4f4c-83c5-482fcf287083)

![Uploading image.png…]()

