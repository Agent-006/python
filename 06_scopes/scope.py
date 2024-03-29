username = "thecoderwiz"

def func():
    # username = "coder"
    print(username)

print(username)
func()

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x 
#     x = 88
    
# func3()
# print(x)

# def f1():
#     x = 38
#     def f2():
#         print(x)
#     # f2()
#     return f2
# result = f1()
# result()
# print(result)

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

result = chaicoder(2)
print(result(2))
print(result)
