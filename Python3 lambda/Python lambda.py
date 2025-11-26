f = lambda : print('Hello Lambda!')
print(f())

y = lambda a: a**2
print(y(5))


t = lambda a,b: a*b
print(t(4,5))

x = lambda a,b,c: a+b+c
print(x(4,5,6))

#将 function 应用于 iterable 中的每一个元素，返回一个 map 对象（可迭代），通常需要转为 list 查看结果。
numbers = [1,2,3,4,5]
result = list(map(lambda x: x**2, numbers))
print(result)

def square(x):
    return x**2

result = list(map(square, numbers))
print(result)

#用 function 对 iterable 中每个元素做判断（返回 True 或 False），保留使函数返回 True 的元素，返回一个 filter 对象。
words = ["apple", "", "banana", "", "cherry"]
results = filter (lambda x: len(x)>0, words)
results1 = filter(None, words)
print(list(words))
print(list(results))
print(list(results1))
numbers = [1,2,3,4,5]
results = filter(lambda x: x%2 != 0, numbers)
print(list(results))
def is_even(x):
    return x%2 == 0
is_even_numbers = filter(is_even, numbers)
print(list(is_even_numbers))


#用 reduce 函数对 iterable 中元素做累计操作，返回一个单一值。
#reduce() 不是内置函数，在 Python 3 中需要从 functools 模块导入。
#它对 iterable 中的元素累积地应用函数，最终返回一个单一值。
from functools import reduce
numbers = [1,2,3,4,5]
result = reduce(lambda x,y: x+y, numbers)
print(result)

#用 lambda 表达式定义一个函数，并将其作为参数传递给另一个函数。
def apply_twice(func, arg):
    return func(func(arg))

result = apply_twice(lambda x: x+2, 3)
print(result)

from functools import reduce
str_list = ['H', 'e', 'l', 'l', 'o',' ', 'W', 'o', 'r', 'l', 'd', '!']
result = reduce(lambda x,y: x+y, str_list)
print(result)

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]
result = list(map(lambda x,y: x+y, list_1, list_2)) 
list_3 = list_1 + list_2
result_even = list(filter(lambda x: x%2==0, list_3))
result_square = list(map(lambda x: x**2, list_3))
result_total = reduce(lambda x,y: x+y, list_3)
print(sum(list_3))
print(result)
print(result_even)
print(result_square)
print(result_total)

#如果你习惯函数式编程风格，这三个函数会非常有用！但在实际开发中，有时列表推导式（list comprehension）更简洁易读，例如：
total = sum(x**2 for x in list_3 if x % 2 == 0)





#partial 是 Python 中 functools 模块里的一个非常有用的函数，用于部分应用（partial application）。它可以把一个函数的某些参数预先固定，生成一个新的函数，新函数只需要传入剩余的参数即可。
#示例 1：固定部分参数
from functools import partial
def my_func(x, y, z):
    return x * y * z
my_new_func = partial(my_func, 2, z=3)
print(my_new_func(4))  # 输出 24

#示例 2：配合 map 使用

def power(base, exponent):
    return base ** exponent

numbers = [2, 3, 4]
print(list(map(lambda x: power(x, 2), numbers)))
result = list(map(partial(power, exponent=2), numbers))
print(result)

#示例 3：替代 lambda
def greet(name, greeting):
    return f"{greeting}, {name}!"
print(greet("Alice", "Hello"))  # 输出 "Hello, Alice!"
greet_phil = partial(greet, "Phil!")
print(greet_phil("Hi"))  # 输出 "Hi, Phil!"

morning_greeting = lambda str: greet (str, "Good morning")
print(morning_greeting("John"))  # 输出 "Good morning, John!"

def add_multiple(x, y, z=1):
    return (x + y) * z
add_multiple_2 = partial(add_multiple, z=2)
print(add_multiple_2(2, 3))  # 输出 10

numbers = [1, 2, 3, 4, 5]
result = reduce(add_multiple_2, numbers)   
#相当于
# (1+2)*2 = 6
# (6+3)*2 = 18
# (18+4)*2 = 44
# (44+5)*2 = 98
print(result)  

#与 lambda 的区别
#lambda 更适合匿名、简单的函数
#partial 更适合已有函数的参数固定，逻辑更清晰，且支持关键字参数
#总结 partial 是函数式编程中的一个重要工具，能让你更灵活地复用函数，减少重复代码。当你发现某个函数的某些参数是固定的，但又不想每次都传入这些参数时，partial 就派上用场了。
