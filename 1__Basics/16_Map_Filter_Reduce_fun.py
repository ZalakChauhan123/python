# All 3 functions are Higherorder fucntions.
# It means they take functions as an argument

"""
Map Function
------------
--- Syntax = Map ( (logic in terms of function), list of elements )
--- Simple use case = Create list-A in which all the elements are squared of list-B 
"""

list_1 = [1,2,3,4,5]

# Logic function
def squareFun (x):
    return x*x

list_2 = map(squareFun,list_1)

print(list_2)

# Map method gives "Object" & we have to convert in into list
afterMap_list_1 = list(list_2)

print(afterMap_list_1)

#-------------------------------------------------

"""
Filter Function
---------------
SYNTAX - Same as Map Function
Behaviour - By filter each element of the list check by function (given as argument)
                     if it true then it will add in a new line
"""

# Using list_1 as an example

list_3_after_filter = list(filter(lambda x: x>2 ,list_1))
print(list_3_after_filter)
# We can use direct lambda func. as a Logic function
# I doesn't create new variable for converting Object of filter to List




"""
REDUCE Function
---------------
SYNTAX - same as map function
Behaviour - It takes all the elements of the list and reduce it in a single value
Simple example - doing Sum or multiplication of list elements
"""
from functools import reduce
# Using list_1 as an example

list_4_after_reduce = reduce(lambda x,y:x+y , list_1)
print(list_4_after_reduce)



