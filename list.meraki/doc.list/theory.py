# Adding Elements to a List
# Using insert() method

# append() method only works for the addition of elements at the end of the List,
# for the addition of elements at the desired position, insert() method is used. 
# Unlike append() which takes only one argument, the insert() method requires
# two arguments(position, value). 

# Using append() method

# Elements can be added to the List by using the built-in append() function.
# Only one element at a time can be added to the list by using the append() method, 
# for the addition of multiple elements with the append() method, loops are used. 
# Tuples can also be added to the list with the use of the append method because tuples are immutable.
# Unlike Sets, Lists can also be added to the existing list with the use of the append() method.

# Using extend() method

# Other than append() and insert() methods, there’s 
# one more method for the Addition of elements, extend(),
# this method is used to add multiple elements at the same time at the end of the list.

# Using remove() method

# Elements can be removed from the List by using the built-in remove() function but an
# Error arises if the element doesn’t exist in the list. Remove() method only removes one element 
# at a time, to remove a range of elements, the iterator is used. The remove() method removes the 
# specified item.
# Note – Remove method in List will only remove the first occurrence of the searched element.

# Using pop() method

# Pop() function can also be used to remove and return an element from the list,
# but by default it removes only the last element of the list, 
# to remove an element from a specific position of the List,
# the index of the element is passed as an argument to the pop() method.

# Slicing 
 
# to print a specific range of elements from the list, we use the Slice operation.
# Slice operation is performed on Lists with the use of a colon(:).
# to print the whole List in reverse order, use [::-1].

# Index starts from 0 and it assign position to the elements.
# Indexing let us know the position of the elements.

# Append()Add an element to the end of the list
# Extend()Add all elements of a list to another list
# Insert()Insert an item at the defined index
# Remove()Removes an item from the list
# Pop()	Removes and returns an element at the given index
# Clear()Removes all items from the list
# Index()Returns the index of the first matched item
# Count()Returns the count of the number of items passed as an argument
# Sort()Sort items in a list in ascending order
# Reverse()Reverse the order of items in the list
# copy()Returns a copy of the list

# n=int(input("Enter the number: "))
# i=0
# while i<=n:
#     if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#         print(i)
#     if i==0 or i==3 or i==5 or i==7:
#         print(i)
#     i+=1
    
