def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("开始执行")
        result = func(*args, **kwargs)  # 调用原函数
        print("执行结束")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))  # 输出：8