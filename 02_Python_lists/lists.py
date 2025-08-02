numbers = [5,2,1,7,4]
print("Original list:")
print(numbers)

print("\n")

# add item at the end of the list
numbers.append(20)
print("After appending 20:")
print(numbers)

print("\n")

# insert items at particular index
numbers.insert(3,9)
print("After inserting 9:")
print(numbers)

print("\n")

# delete or remove a particular item from a list
numbers.remove(20)
print("After removing 20:")
print(numbers)

print("\n")

# to remove last element from the list use pop()
numbers.pop()
print("After popping one element:")
print(numbers)

print("\n")

# to check for index of first occurence of an element
print("Index of 5 is:")
print(numbers.index(5))

print("\n")

# to check existence of an item
print("Does 50 exist in the list:")
print(50 in numbers)

print("\n")

# to count occurences of an element
print("How many times 5 exists in the list:")
print(numbers.count(5))

print("\n")

# to sort the list
numbers.sort()
print("After sorting the list:")
print(numbers)

print("\n")

# to create a copy of the list 
nums = numbers.copy()
print("New copy of the list, which is independent of the original list:")
print(nums)

print("\n")

print("original list:")
print(numbers)

print("\n")

# to remove all elements use clear() method
numbers.clear()
print("After clearing all elements from the list:")
print(numbers)
