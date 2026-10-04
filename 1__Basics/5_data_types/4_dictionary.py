# Duplicate key is not allowed. it overwrite the key
countries = {
    "nation-1":"India",
    "nation-2":"China",
    "nation-3":"USA",
    "nation-3":"USA",
    "nation-5":"Germany"
}
print(countries)
# Print specific value based on key
print(countries["nation-2"])



# Create Dic. using dict() constructor
# NOTE = Instead ":" use "=" between Key and value
dic_2 = dict(name="Zalak" , age=25 , Gender="male" , country="India" , state="Gujarat" ) 
print(dic_2)

#  ------- Accessing Iteams -------
a = dic_2.get("Gender")
print(a)

# keys() & values(). It return in the foam of "List"
b = dic_2.keys()
print(b)
c = dic_2.values()
print(c)
# items() = It return list of key value in a "Tuple"
d = dic_2.items()
print(d)


# To check specific items in the list. 
# Use key to find it as a string
if "state" in dic_2:
    print("---- Yes , Available ----")




#  ------- Update Items -------
# Only 1 method Update()

dic_3 = {
    1:"one",
    2:"Two",
    3:"THree",
    4:"Four"
}
dic_3.update({3:3.00})
print(dic_3)

dic_another = {5:"Five" , 6:"Six" , 7:"Seven"}
dic_3.update(dic_another)
print("Dic - 3 :- ",dic_3)


# NOTE :- This method modifies existing dictionary in above example it modify dic_3 




#  ------- Add Items -------
dic_4 = {
    1:"Red",
    2:"Green",
    3:"Yellow",
    4:"Black"
}
dic_4[6] = "Blue"
print("Dic-4 :-",dic_4)
print(dic_4[6])


#  ------- Delete Items -------
# pop() = it delete element based on given key value
dic_4.pop(1)

if 1 in dic_4:
    print(dic_4[2])
else:
    print("Not Available")



#  ------- Loop throw Dictionary -------
for dic_4_keys in dic_4.keys():
    print("dic_4_keys - ",dic_4_keys)

for dic_4_values in dic_4.values():
    print("dic-4-values-" , dic_4_values )

for dic_4_items in dic_4.items():
    print("Item - " , dic_4_items)

