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