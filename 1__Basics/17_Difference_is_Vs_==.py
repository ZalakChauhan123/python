"""
--- Is and "==" both are comparison operator


--- IS Operater
--- it check  ---two variables---  refer to the  ---same object---  in memory.
--- it gives exect location of the object.

"""



x = [1,2,3]
y = x        # y point out same obj. as x
z = [1,2,3]  # z is a different obj. with same content

print (x is y)  # Gives True, because x & y both refers same obj. which is [1,2,3]
print(x is z)   # Gives False, because x & z refers different obj. althought content is same


"""
== Operater

--- it check  ---two variables---  refer to the same value
--- it checks content

"""

# QUESTION IS VALUE
x = [1,2,3]
y = x       # point out same value as x 
z = [1,2,3] # different variable with same content

print(x==y) # True, because value in x & y is same
print(x==z) # True, because value in x & z is same

