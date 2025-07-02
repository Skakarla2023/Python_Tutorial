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
