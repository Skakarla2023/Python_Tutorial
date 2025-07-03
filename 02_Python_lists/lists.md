# List

- Lists are used to store multiple items in a single variable.
- Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

-------------------------------------------------------------------------------------------------------------------------

![image](https://github.com/user-attachments/assets/91f1a0c5-1ab3-44fc-8141-bd9960224fc0)

### List Items

- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc.

### Ordered

- When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
- If you add new items to a list, the new items will be placed at the end of the list.

### Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

### Allow Duplicates
Since lists are indexed, lists can have items with the same value.

- the following python code describes the basic functions in lists like adding,removing, modifying list elements:

```python
thislist = ["apple", "banana", "cherry", "apple", "cherry","watermelon","pineapple","kiwi","papaya"]

print(thislist)
print("\n")

# accesing list items
print(thislist[3])
print("\n")
print(thislist[-2])
print("\n")
print(thislist[1:3])
print("\n")
# modifying the list items
thislist[1]="apricot"


# adding new values
thislist[5]="coconut"

# removing specific value
thislist.remove("cherry")

# loop through lists
for i in thislist:
	print(i)

print("\n")
    
# looping using index numbers
for i in range(len(thislist)):
	print(thislist[i])

print("\n")

# sorting lists
thislist.sort()

# you can sort a list in descending order using the reverse keyword
thislist.sort(reverse=True)

print(thislist)
```

Output:
```
['apple', 'banana', 'cherry', 'apple', 'cherry', 'watermelon', 'pineapple', 'kiwi', 'papaya']


apple


kiwi


['banana', 'cherry']


apple
apricot
apple
cherry
coconut
pineapple
kiwi
papaya


apple
apricot
apple
cherry
coconut
pineapple
kiwi
papaya


['pineapple', 'papaya', 'kiwi', 'coconut', 'cherry', 'apricot', 'apple', 'apple']
```

![image](https://github.com/user-attachments/assets/1db8b287-acf3-4d9d-bab9-68e1dae643b3)

- Without list comprehension you will have to write a for statement with a conditional test inside:

```python
fruits=["apple","banana","kiwi","mango","orange"]
newlist=[]

for x in fruits:
  if "a" in x:
    newlist.append(x)
        
print(newlist)
```

Output:
```
['apple', 'banana', 'mango', 'orange']
```

- With list comprehension you can do all that with only one line of code:

```python
fruits=["apple","banana","kiwi","mango","orange"]
newlist=[x for x in fruits if "a" in x]        
print(newlist)
```

output:
```
['apple', 'banana', 'mango', 'orange']
```

![image](https://github.com/user-attachments/assets/ea502f46-0195-4a74-a93b-51bfbaa18562)

![image](https://github.com/user-attachments/assets/f3e87701-c0ee-4e6d-bed1-8bf86dde6b0e)


![image](https://github.com/user-attachments/assets/e0c00e0b-8754-4438-a010-53af382dfa2f)

![image](https://github.com/user-attachments/assets/d2d5b09c-058d-43da-8249-999cffba715e)

output:
```
[50, 65, 23, 82, 100]
```

### Case Insensitive Sort

By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

![image](https://github.com/user-attachments/assets/83e192ce-3023-4d8a-88bf-ca292ee7e2b3)

![image](https://github.com/user-attachments/assets/ebf7f6fa-df34-4732-9458-83c59e900320)

![image](https://github.com/user-attachments/assets/909b5008-0b24-46f9-9a5a-5be7c4062000)

![image](https://github.com/user-attachments/assets/27c26ba0-b45d-438c-bbf5-85e050621701)

```python
# copying a list using different methods
thislist = ["apple", "banana", "cherry"]

#by slicing the list
mylist = thislist[:]

#by using the copy() method
mylist1=thislist.copy()

#by using built-in list method
mylist2=list(thislist)

# printing all the new lists

print(mylist)
print(mylist1)
print(mylist2)
```

output:
```
['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry']
```

![image](https://github.com/user-attachments/assets/697efed1-ff67-481d-bcd2-6aaf6a029762)

```python
list1=[1,2,3]
list2=["a","b","c"]

#using the concatenation operator
list3=list1+list2
print(list3)

#using the built-in extend() method
list1.extend(list2)

#by appending one list elements into other
for i in list1:
	list2.append(list1)
    
print(list2)
```

output:
```
[1, 2, 3, 'a', 'b', 'c']
['a', 'b', 'c', [1, 2, 3, 'a', 'b', 'c'], [1, 2, 3, 'a', 'b', 'c'], [1, 2, 3, 'a', 'b', 'c'], [1, 2, 3, 'a', 'b', 'c'], [1, 2, 3, 'a', 'b', 'c'], [1, 2, 3, 'a', 'b', 'c']]
```












```python

```

output:
```

```
