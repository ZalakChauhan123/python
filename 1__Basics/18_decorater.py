# Create decorate function 
def greet(function):

    # This func. inside greet
    def modified_function(*args , **kwargs):
        function(*args , **kwargs)
        print('Thank You for using this function')
    return modified_function

# ------------------------------------------------------------------

@greet # --->> Using Decorater
def addition(a,b):
    print(f"Addition of Given Number is {a+b}")

# Calling addition func.
addition(10,20)


# ------------------------------------------------------------------


@greet # --->> Using Decorater
def hello ():
    print("Hello")

# Calling hello func.
hello()

