def max(a,b):
    if a > b:
        return a
    else:
        return b
    
a = 8
b = 5

print (max(a,b))

def Hello():
    print("Hello World!")

Hello()


def area(w,h):
    return w*h
def print_welcome(name):
    print(f'Welcome {name}!')

w = 3
h = 4
a = area(w,h)
print(f'面积是: {a}!')
print_welcome('Phil')

def printme(str):
    print(str)
    return
printme("Hello")
printme("Phil")


def changelist(mylist):
    mylist.append([10,20,30])
    print(f'函数内取值： {mylist}')
    return
mylist1 = [1,2,3]
changelist(mylist1)
print(f'函数外取值： {mylist1}')

def printinfo(name,age = 39): #默认参数必须放在最后面，否则会报：
    print(f'Your name is {name}')
    print(f'Your age is {age}')
    return
printinfo(age = 20, name = "Phil")
printinfo(name = "Phil")

def printinfo1(arg1, *arg2):
    print(f'正常参数是： {arg1}')
    print(f'不定长参数是：{arg2}')
    return
printinfo1(10,20,30,40)
    
def printinfo2(arg1,*vartumple):
    print(f'正常参数是： {arg1}')
    for var in vartumple:
        print(f'不定长参数是： {var}')
    return
printinfo2(1,2,3,4,5,6)

def pirntinfo3(arg1,**vardic):
    print(arg1)
    print(vardic)

pirntinfo3(3,a=4,b=5,c=8)

def fn(a,b,*,c): #*：是一个语法分隔符，表示 * 后面的所有参数必须以关键字形式传入。

    return a+b+c
print(fn(1,2,c=4))

x = lambda a,b,c: a*b*c
print(x(1,2,3))


def func(n):
    return lambda a: a*n # 匿名函数（lambda）
mydoubler = func(2) #用匿名函数创建两个新函数
mytrippler = func(3) #用匿名函数创建两个新函数

print(mydoubler(11))
print(mytrippler(11))

def sum(arg1,arg2):
    total = arg1 + arg2
    print(f'函数内:{total}')
    return total

total = sum(20,30)
print(f'函数外:{total}')