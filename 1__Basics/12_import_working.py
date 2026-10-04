# Basic Importing
# Importing test_1 file & use all properties and functions by adding . operater
import test_1 as t1

result = t1.str_1
print(result)

print(t1.addition(5,10))




# For import multiple functions & variables from single file
from test_1 import str_1, str_2, addition

print(str_1)
print(addition(4,5))
print(str_2)