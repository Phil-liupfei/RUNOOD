def my_decorator(fun):
    def wrapper():
        print('调用前')
        fun()
        print('调用后')
    return wrapper

@my_decorator
def sy_hello():
    print('Hello Phil')

sy_hello()


def my_decorator2(fun):
    def wrapper(*args1,**kwargs):
        print('Before')
        results = fun(*args1,**kwargs)
        print('After')
        return results
    return wrapper
#调用
@my_decorator2
def add(a,b):
    return a + b
print(add(3,4))
