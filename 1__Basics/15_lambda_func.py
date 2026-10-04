"""
What is Lambda function :- It is single line function
"""
# SYNTAX :- Variable_name = lambda argument1, argument2 : return


# Normal way of create average function
def avgOfNumbers (a,b):
    return (a+b)/2
# Calling fun.
print(avgOfNumbers(5,5))


# This same thing we can do in single line of code
avgFunc = lambda a,b: (a+b)/2
print(avgFunc(5,5))