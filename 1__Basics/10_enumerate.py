# enumerate function :- function that simplifies looping through keeping track of 
# both the index and the value of each item in the iterable.


# Example-1
# fruits = ["Apple" , "Banana" , "Grapes" , "Papaya"]
# for index,value in enumerate(fruits):
#     print(index,value)



# Example-2
marks = [10,20,30,40,50]
for index,i in enumerate(marks):
    if(index==2):
        print("This is Index Two")
    print(index,i)