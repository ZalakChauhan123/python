"""
👌 WHAT IS Generators

-- A function becomes a generator when it uses the yield keyword instead of return. 
-- Calling it returns a generator object, not a value
-- Every time you iterate (e.g., with for or next()), the function runs until it hits yield, 
   returns that value, and pauses, preserving its local state for when you resume 🚀
"""

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Usage:
for num in count_up_to(5):
    print(num)  # prints 1,2,3,4,5