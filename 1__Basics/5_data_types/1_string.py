# --- STRING --- DATA TYPE

# string_1 = "Computer Science"
# print(string_1)
# print(type(string_1)) # for find data type



multi_line_sring = '''
Geeks
For
Geeks
'''
print(multi_line_sring)



# Find Character at specific Position
a = "Hello world"
print(a[2])



# # Looping throw String
string4 = "Advantages"
for x in string4:
  print(x)



# in & not in Keyword 
# It return True, False flag
string5 = "You can get free coupons"
print("get" in string5)
print('gettttt' not in string5)




# Slicing of String - Get Characters in specific range
string6 = "Hello World"
print(string6[1:4]) # answer= ell
# NOTE :- index 1 is starting range & index 4 in ending range which is excluded
print(string6[-5:-1]) # answer= Worl
# NOTE :- index -5 is ending range & index -1 is starting range which is      excluded
print(string6[2:]) # answer= llo World
print(string6[:5]) # answer= Hello
# NOTE :- index 5 is excluded



string7 = "zalak"
string8 = "ZALAK"
print(string7.upper() , string8.lower())



# Remove Whitespaces & replace something with something & split string
string9 = " He llo Worl d , i am zalak "
Without_space_string9 = string9.replace(" ","")
updated_string9 = Without_space_string9.replace(",",":")
print(updated_string9)

list_of_updated_string9 = updated_string9.split(':')
print(list_of_updated_string9)
print(list_of_updated_string9[0])



# concatinating string and integar using f-string method
char1 = "Zalak"
char2 = 45

print(f"{char1} {char2}")



# Other methods

# find() = it return index value of given string
string10 = "In norway vikings were very danger in 1980"
print(string10.find("were"))
print(string10.index("were"))
# NOTE :- only difference between above 2 methods is that find() method will return -1 if given string is not present in string whereas index() method will throw an error


# count() = it return character count of given string
print(string10.count("vikings"))