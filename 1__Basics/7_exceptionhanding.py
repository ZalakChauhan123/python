# try:
#     a = int(input("Enter any number :-"))
#     print(a)
# except Exception as e:
#     print(e)

# print("Some other lines of Code...")



# # We can handle multiple errors by adding multiple exceptions
# try:
#     b = [5,10]
#     print(c[15])
# except ValueError:
#     print("Value error")
# except IndexError:
#     print("Index Error")
# except Exception as e:
#     print(e)

# print("Some Lines other of Code is Running ----")




"""
finally 
:- It always executed irrespective of Errors occoured in try / except block or not
:- It always executed after try , except block
:- Commonly used to release resources like files, database connections, or network sockets, ensuring proper cleanup in all situations.


-------- Try this example in future --------
try:
    file = open("example.txt", "r")
    # Some code that may raise an exception
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()  # This will execute whether or not an exception occurred

"""

c = [5,10,15,20]
custom_index = int(input("Enter any index :- "))

try:
    print(c[custom_index])
except:
    print("Some Error Occured...")
finally:
    print("--- IT IS ALWAYS EXECUTED ---")








