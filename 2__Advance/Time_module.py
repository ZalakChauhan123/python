import time as time

# localtime() -- for getting local time
find_local_time = time.localtime()
print(find_local_time)

# strftime() -- for modify time values
formated_time = time.strftime("%Y-%m-%d %H:%M:%S", find_local_time)
print(formated_time)


# sleep() -- wait execution of code for given time
x = 5
print("This line execute after 3 seconds")
time.sleep(3)
print(x)

