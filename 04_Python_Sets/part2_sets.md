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
