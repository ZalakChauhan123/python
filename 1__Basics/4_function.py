# a = int(input("Enter Num-1 - "))
# b = int(input("Enter Num-2 - "))
# c = int(input("Enter Num-3 - "))

# def grater_outof_three(num1, num2, num3):
  
#   if(num1>= num2 and num1>= num3):
#     print(f'{num1} is Grater')
#   elif(num2>=num1 and num2>= num3):
#     print(f'{num2} is Grater')
#   else:
#     print(f"{num3} is Grater")

# grater_outof_three(a,b,c)

# In functions there are  4 types of arguments

# 1. Required Arguments
# 2. Default Arguments
# 3. Keyword Arguments
# 4. Variable length Arguments


# Required Arguments
# In this type of arguments we have to give the value of the arguments in the function calling.

# in this case a & b is required arguments
# def Plus (a,b):
#   return a+b

# # Function calling
# x = Plus(10,20)
# print(x)



# # Variable Length Argument
# def Average(*numbers):
#   print(type(numbers))
#   sum = 0
#   for i in numbers:
#     sum = sum + i
#   print(f"Average is :- {sum/len(numbers)}")

# Average(2,4,6,8,10)






# Find Highest Numbers out of infinite given argument
def Find_highest_number(*numbers):
  max_number = numbers[0]
  for i in numbers:
    if(i>max_number):
      max_number = i
  return max_number

# Function Calling
print(Find_highest_number(-4,5,10,100,8,99,42,-1))





# Find Plus operation for infine given argument to function
def Plus_of_numbers(*numbers):
  total_num = 0
  for i in numbers:
    total_num = total_num+i
  return total_num

# Function calling
print(Plus_of_numbers(1))
    

     