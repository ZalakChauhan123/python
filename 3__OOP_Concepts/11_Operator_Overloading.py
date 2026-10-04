"""
OPERATOR OVERLOADING

The feature that allows you to define or change the behavior of 
built-in operators (like +, -, *, ==, etc.) for your own classes.

By use of Dunder or magic methods we can define or change the behaviour of operators

"""

# for example
a = 2
b = 3
print(a+b) # 5
print(a.__add__(b)) # It gives same result 5



# Example for change the behaviour of "+" operator
"""
Normally, + would concatenate strings (e.g., "Hello" + "World" → "HelloWorld").
Here, for the Word class, + joins the words with a dash ("Hello-World").
This proves the behavior of + is changed for this class.
"""

class Word:
    def __init__(self, text):
        self.text = text
    
    # This method change the behaviour of the operator "+"
    def __add__(self, other):
        
        # It return New Object of Word class
        # self.text =  operand-1 (before + operator)
        # other.text = operand-2 (after + operator)
        return Word(self.text + "-" + other.text)
    
    # Convert return object into string
    def __str__(self):
        return self.text

w1 = Word("Hello") # operand-1
w2 = Word("World") # operand-2
w3 = w1+w2 # calls __add__ method inside Word class
print(w3)




