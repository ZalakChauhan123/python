def get_input():
    user_input = input("Enter number between 1 to 10 :- ")

    if(user_input == "quit"):
        return "Program Closed..."
    try:
        convert_user_input = int(user_input)
        if(convert_user_input<1 or convert_user_input>9):
            raise ValueError("Number must be between 1 and 10.")
    except ValueError:
        raise ValueError ("Invalid Input ")
    
    return user_input


# Calling get_input()
print(get_input())
