# Python Sets

![image](https://github.com/user-attachments/assets/87ca1495-b3a7-4d7a-a75d-b964f9d62521)

```python
myset={"apple","banana","cherry"}
print(myset)
```

Output:
```
{'banana', 'apple', 'cherry'}
```

![image](https://github.com/user-attachments/assets/2198acdf-ea73-468d-9d21-dfe5c5e07588)

![image](https://github.com/user-attachments/assets/09819ff6-8abc-42fc-9839-50d9aee06a1a)

![image](https://github.com/user-attachments/assets/54929ae2-5636-464e-a76a-4b9f95f8f6bb)

![image](https://github.com/user-attachments/assets/e9225d34-2ffe-4e2f-967a-43b38cf3782a)

```python
thisset = {"apple", "banana", "cherry","cherry"}

print(thisset)
```

Output:
```
{'cherry', 'banana', 'apple'}
```

![image](https://github.com/user-attachments/assets/89615a97-4f3a-4b02-b4ac-69cb33b5ae93)

![image](https://github.com/user-attachments/assets/4e374031-e7e3-4ff0-a2ab-4938e61493ff)

```python
thisset = {"apple", "banana", "cherry",False,True,1,0}

print(thisset)
```

Output:
```
{False, True, 'cherry', 'banana', 'apple'}
```

![image](https://github.com/user-attachments/assets/65ae4fdb-a588-4b42-b8ee-984d15cc3450)

![image](https://github.com/user-attachments/assets/a6bf5452-35ad-4f4a-90cd-fda4e0798960)

A set can contain different data types:

```python
set1={1,"apple",True}
print(set1)
```

Output:
```
{1, 'apple'}
```

![image](https://github.com/user-attachments/assets/04bbe1cf-e23e-446b-bf78-edf34d0c0bb1)

```python
set2={1,2,3}
print(type(set2))
```

Output:
```
<class 'set'>
```

![image](https://github.com/user-attachments/assets/fe88c5a7-eb21-4980-b82f-198a536ac22b)

```python
myset=set((1,2,3,4,5))
print(myset)
print(type(myset))
```

Output:
```
{1, 2, 3, 4, 5}
<class 'set'>
```

![image](https://github.com/user-attachments/assets/695cefcc-1fa7-43ab-9e38-2c1a1b3b2d16)

```python
myset={1,2,3,4,5}

for i in myset:
	print(i)
```

Output:
```
1
2
3
4
5
```

- Check if an element is present in the set:

```python
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```

Output:
```
True
```

- Check if an element is present not in the set:

```python
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
```

Output:
```
False
```

![image](https://github.com/user-attachments/assets/e2bdfc4b-dba1-4239-9c88-1111802813df)


- To add one item to a set use the add() method.

```python
myset={1,2,3,4,5}

myset.add(6)
myset.add(7)

print(myset)
```

Output:
```
{1, 2, 3, 4, 5, 6, 7}
```

![image](https://github.com/user-attachments/assets/bc0308b4-f97f-4264-bb85-30644b5bca57)

```python
s1={"a","b","c"}
s2={"d","e","f"}


# this method updates the current set by adding the other set elements
s1.update(s2)

print(s1)
```

Output:
```
{'a', 'b', 'c', 'f', 'e', 'd'}
```

![image](https://github.com/user-attachments/assets/743896f4-7cf1-4566-810d-9bbfb496d04e)

```python
s1={"a","b","c"}

# another set
s2={"d","e","f"}

# another list
mylist=["g","h","i"]

#another tuple
mytuple=("j","k","l")


s1.update(s2)
print(s1)

s1.update(mylist)
print(s1)

s1.update(mytuple)
print(s1)
```

Output:
```
{'a', 'e', 'f', 'c', 'b', 'd'}
{'h', 'i', 'b', 'c', 'g', 'a', 'e', 'f', 'd'}
{'h', 'i', 'b', 'j', 'c', 'g', 'a', 'e', 'f', 'l', 'd', 'k'}
```

![image](https://github.com/user-attachments/assets/12c2a5b3-1ef8-4bf5-82ae-9df50415a590)

```python
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
```

Output:
```
{'cherry', 'apple'}
```

![image](https://github.com/user-attachments/assets/e209836c-f460-4526-9fa4-3cf3733dac86)

- If the item specified in remove does not exist it will raise an error.

```python
thisset = {"apple", "banana", "cherry"}

thisset.remove("kiwi")

print(thisset)
```

Output:
```
Traceback (most recent call last):
  File "./prog.py", line 3, in <module>
KeyError: 'kiwi'
```

- Use the discard() method, if the item specified in the discard method does not exist, it does not return an error.

```python
thisset = {"apple", "banana", "cherry"}

thisset.discard("cherry")
print(thisset)
```

Output:
```
{'banana', 'apple'}
```

![image](https://github.com/user-attachments/assets/266e7d16-9f8c-4512-b749-45df4443b00e)

```python
thisset = {"apple", "banana", "cherry"}

thisset.discard("kiwi")
print(thisset)
```

Output:
```
{'banana', 'cherry', 'apple'}
```

![image](https://github.com/user-attachments/assets/7bdc9709-89b8-49a2-b571-79d8ce838212)

```python
myset={"a","b","c","d"}

x=myset.pop()
print(x)
```

Output:
```
c
```

![image](https://github.com/user-attachments/assets/5e3ec03e-1a53-4f1f-9d22-008f31cad54f)

- The del keyword will delete the set completely:

```python
myset={"a","b","c","d"}

del myset

print(myset)
```

Output:
```
Traceback (most recent call last):
  File "./prog.py", line 5, in <module>
NameError: name 'myset' is not defined
```


