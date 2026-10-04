# In the open method there are 3 common modes r,w,a (read , write , append)

# OPEN & READ FILE
content = open("11_Virtual_Env.txt" , 'r')
read_file = content.readlines()
print(read_file)
content.close()



# NOTE :- With this method we can't add close statement
# READ FILE
with open ('demofile.txt' , 'r') as content:
    print(content.read())


# WRITE FILE
with open ('demofile.txt' , 'w') as content :
    content.write("\nTHIS IS ANOTHER LINE IN THIS FILE...")



# APPEND CONTENT IN FILE
with open ('demofile.txt' , 'a') as content:
    content.write("Hello World...")


# APPEND & READ FILE
with open ('demofile.txt' , 'a+') as content:
    print(content.write("I AM ZALAK CHUAHAN...."))




"""
Line Counting Program 
:- Counting Lines inside demofile.txt
"""
def CountLineFunc():
    # Open file with read mode
    with open ("D:\python\demofile.txt" , "r") as file:
        # Read entire file
        readfile = file.read()
        # Split line based on \n
        LineCount = readfile.split("\n")
        # Find line count
        print(f"Total Line Count in this File :- {len(LineCount)}")
        
# calling function CountLineFunc()
CountLineFunc()




"""
Word Counting Program 
:- Counting Words inside demofile.txt
"""
def WordCountFunc():
    with open ("demofile.txt" , "r") as file:
        # Read Entire File
        read_content = file.read() 
        # Split Word based on Space
        word_count = read_content.split()
        # Counting the Words
        print(f"The Number of Words in the File :- {len(word_count)}")

# Calling function WordCountFunc()
WordCountFunc()


# Reading Mehtods :- read() , readline() , readlines()

# read() ---> By this method we can read entire txt file
with open ("F:\python\demofile.txt" , "r") as content:
    # read that opened file
    readFile = content.read()
    print(readFile)

# readline() ---> By this method we can read 1 line from text file
with open ("demofile.txt" , "r") as content:
    readFile = content.readlines()
    print(readFile[0])


# readlines() ---> This method gives list of strings
def readLinesMethod_Func():
    with open ("F:\python\demofile.txt" , "r") as content:
        # read file
        readFile = content.readlines()
        print(readFile[0])

# Calling func
readLinesMethod_Func


