"""
Walrus Operator - Used to assign a value to a variable within an expression.

Syntax -  ":="

variable := expression
This assigns the result of expression to variable, and returns the value as well.
"""

data = input("Enter something :-")

while data != "Exit":
    print(f"You Entered {data}")


# With Walrus Operator
while (data != input("Enter something :- ")) != "Exit":
    print(f"You Entered {data}")