print("Hello World")
i = 256*256
print(f'i的值为 {i}')

my_list = ['google', 'runoob', 'taobao']
print(f'my_list的第一个元素是: {my_list[0]}') # 输出 "google"
print(f'my_list的第二个元素是: {my_list[1]}') # 输出 "runoob"
print(f'my_list的第三个元素是: {my_list[2]}') # 输出 "taobao"

for i in range(5):
    print(i, end=' ')
print()
print('------------------------------------------------')
i = 15
while i < 10:
    print('i小于10')
else:
    print('i大于10')

#!/usr/bin/python3
 
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b