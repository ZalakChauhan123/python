tup1 = (1,2,3,4,5,6,7,8,9,10)

# To create tuple with single element
# NOTE :- it is compulsory to add , after 1st element, otherwise python consider it as a veriable 
tup_empty = (1,)
print(type(tup_empty))


# Accessing element in tuple
print(tup1[0:5]) # 1,2,3,4,5
print(tup1[-2]) # negetive indexing
print(tup1[len(tup1)-2])  # Postive Indexing
print(tup1[2:5]) # 3,4,5



# Cheking of specific element in the tuple
if 10 in tup1:
  print("Yes available")
else:
  print("Not available")


# Update Tuple
"""
It is possible to update tuple by converting it into list and then update it and then convert it back to tuple
"""
tup2 = (1,2,3,4,5)
print(type(tup2) , tup2)
# Convert from Tuple to List
tup_to_list = list(tup2)
print(type(tup_to_list),tup_to_list)
# Add elemnt
tup_to_list.append(100)
print(tup_to_list)
# Convert back in list
tup_to_list = tuple(tup2)
print(type(tup2))

"""
Similarly we can perform Delete operation as well
"""


# Concatenation of Tuple
t3 = (1,2,3)
t4 = (4,5,6)
t5 = t3 + t4












