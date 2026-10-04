"""
FUNCTION CACHING -- It stores result of function call, 
so that we can reuse it instead of recomputing next time for same argument 

"""


from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(x):
    time.sleep(3)
    return x*5

# It's takes time of 5 second to print result
print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(5))
print("Done for 5")


# No Time for Below Computation
# WHY --> It shows result from Cache. Python doesn't calculate results again , bcs Domain (argument) is same
print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(5))
print("Done for 5")
# Adding New Value --> Now, It takes time for below result
print(fx(2))
print("Done for 2")

