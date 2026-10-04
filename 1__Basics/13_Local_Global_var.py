a = 10
print("Global a - " , a)

def fun_1():
    global a
    a = 700
    print("Modified Global a inside Function - " , a)
    b = 20
    print("Local b inside function - " , b)

fun_1()
print("Global a outside function - " , a)
