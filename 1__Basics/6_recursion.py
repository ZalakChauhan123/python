"""
In simple words recursion is the process of defining something in itself.
Here , i am calling function inside the function body
"""

# Factorial Program
# factorial(5) = 5 * 4 * 3 * 2 * 1
# factorial(4) = 4 * 3 * 2 * 1
# ... factorial(1) = 1 & factorial(0) = 1

def factorial(n):
  if(n==0 or n==1):
    return 1
  return n * factorial(n-1) 

 
# print(factorial(5))

# Fibanacci Number Function :-    
def feb_num(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  return feb_num(n-1) + feb_num(n-2)

print(feb_num(5))