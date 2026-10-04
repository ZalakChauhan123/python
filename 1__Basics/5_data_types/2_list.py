list_1 = [10, "Hello" , True , 345 , 9999 , "Zalak" , False , "Python" , "Java" , "C++" , "C#" , "JavaScript" ]

# list Indexing rule are same as string slicing rules...
print(list_1[:4]) # 10 , "Hello" , True , 345
print(list_1[1:-1])
print(list_1[:-1])





print(list_1[-2]) # negetive indexing
"""
How to convert Negetive to Positive Indexing
1. Find length of the list
2. minus it with whatever given negetive index - see below example
NOTE :- IT IS A BEST PRACTICE...
"""
print(list_1[len(list_1)-2])





# ------- list Methods --------

# Insertion operation
l1 = [1,2,3,4,5,6,7,8,9,10]
l1. append(12) # add elemet at the end of the list
l1.insert (1,234) # add element at specific index
print(l1)
# It is 1 of the way to list concatination (Adding 2 lists)
l1.extend([100,200,300])
# 2nd way of list concatination
l2 = [111,222,333]
l3 = [123,456,789]
l4 = l2 + l3
print(l4)



# Removing Elements :- 2 methods remove() & pop()
l10 = ["Apple","Banana","Python","Javascript",1,2,3,4,5,6,7,8,9,10]
l10.remove(1) # it remove given element from the list not index number
l10.remove("Banana")
print(l10)
# pop() method removes based on index element from the list & if no index is given it removes last element from the list
l10.pop(0)
print(l10)



# Sorting
l5 = [10,4,5,67,844,0,-5,9,-1]
l5.sort() # ascending order
# l5.sort(reverse=True) # descending order
print(l5)



# Loop throw list
l12 = [1,2,3,4,5,6,7,8,9,10]
for i in l12:
    print(i)



# List comprehension - Creating 1 list out of another list
l13 = [1,2,3,4,5,6,7,8,9,10]
print("L13 List - ",l13)
new_list_l14_list = []
for i in l13:
  new_list_l14_list.append(i*i)

print("L14 List - ",new_list_l14_list)

l15 = [x+x for x in l13]
print("l15 list - ",l15)



# Change Specific element in list
l16 = [1,2,3,4,5,6,7,8,9,10]
print("L16 Before Change - ", l16)
l16[0] = 1234
print("L16 After Change - ", l16)
