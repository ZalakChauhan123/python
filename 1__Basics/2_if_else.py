# Find largest among 3 Numbers
# 1st is grater than 2 & 3
# 2nd is grater than 1 & 3
# 3rd is grater than 1 & 2

num1 = int(input("Enter Num-1 :- "))
num2 = int(input("Enter Num-1 :- "))
num3 = int(input("Enter Num-1 :- "))

if num1 >= num2 and num1 >= num3:
  print(num1 , "Num1 is grater")
elif num2 >= num1 and num2 >= num3:
  print(num2 , "Num2 in Grater")
else:
  print(num3 , "Number 3 is grater")



