# # PRINT STATEMENT --->> 4 arguments = end,sep,file,flush
# # sep means : It seperate out whatever in print statement.
# print("Hello",1,2,3 ,sep="~")  #output :- Hello~1~2~3

# # end means : add after execution of print statement whatever inside end.
# print("Hello" ,end="Zalak1234")  #output :- HelloZalak1234

# # --- F-STRING --- = formated string literals
# # It is Strig formating. We can add variable in the string.
# name_value="Zalak"
# age_value = 25
# print(f"My name is {name_value} and my age is {age_value}.")
# # Show Curley braces in f-string
# print(f"My name is {{Zalak}}")
# # Print Dictionary using f-string
# Dic_1={"name":"Zalak" , "age":25}
# print(f"My name is {Dic_1['name']} & My age is {Dic_1['age']}.")

# # ---- FORMATING OUTPUT ---------
# # Using Format Method
# print("My name is {} and Your Name is {}".format("AAA" , "BBB"))
# print("Hello {1} , How are you. I am {0}".format("Zalak" , "Mick"))
# print("My name is {Person_2} and Yours is {Person_1}".format(Person_1="CCC" , Person_2="DDD"))

# --- OPERATORS ---
# print(10+20)
# print(20-10)
# print(10*20)
# print(10**3) # Exponential =  10 to the power 3 = 10*10*10=1000
# print(20/15) # Simple Division
# print(20//15) # Floor Division = means it will give only integer value.
# print(5%3) # Modulus = means it will give remainder.

# # --- DATA TYPES ---
# a = 5        # Interger data type
# b = 2.678    # Float data type
# c = "Hello"  # String data type
# d = True     # Boolean data type
# e = None # Absence of Value: None is used to denote that a variable does not have a value.

# --- TYPECASTING ---
# 2 Types = Internal & External
# Internal Typecasting
# a = 10
# b = 5.5
# c = a+b
# print(c , "Data type of c is = ",type(c)) # Python authomatically converts the data type of c from float to int.
# #External Typecasting = Basic 3 methods ---> int() , float() , str()
# c = "1"
# d="2"
# print(c+d) # It is basically string concatination
# print(int(c)+int(d)) # it is called External typecasting

# print('HEllo')
