###Python 推导式

##列表推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
namesnew = [name.upper()for name in names]
new_names = [name.upper()for name in names if len(name)>3]
List1 = [i for i in range(10) if i%2 == 0]

print(f'namesnew: {namesnew}')
print(f'new_names: {new_names}')
print(f'List1: {List1}')

##字典推导式
listdemo = ['Google','Runoob', 'Taobao']
dic_new = {key.lower():len(key) for key in listdemo}
print(f'dic_new: {dic_new}')

dic = {i:i**2 for i in range (9)}
#dic = {x: x**2 for x in (2, 4, 6)}
print(f'dic_new: {dic}')

#1. 简单映射：将列表元素作为键，其平方作为值
num = [1,2,3,4,5,6,7]
dic_num = {x:x**2 for x in num}
print(f'dic_num: {dic_num}')
#2. 字符串处理：统计每个字符的 ASCII 值
word = 'hello'
dic_word = {t:ord(t) for t in word}
print(dic_word)
#3. 过滤条件：只保留偶数键
data = range(1,11)
even_squarer = {x:x**2 for x in data if x%2 == 0}
print(even_squarer)
#4. 从两个列表构建字典（类似 zip）
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'Beijing']
info = {k:v for k, v in zip(keys,values)}
info1 = dict(zip(keys,values))
print(info)
print(info1)
#5. 反转字典（键变值，值变键）
original = {'a': 1, 'b': 2, 'c': 3}
reversed_dic = {v:k for k, v in original.items()}
print(reversed_dic)
#6. 处理嵌套数据：提取学生姓名和成绩
students = [
    {'name': 'Tom', 'score': 88},
    {'name': 'Jerry', 'score': 92},
    {'name': 'Spike', 'score': 75}
]
score_dic = {s['name']:s['score'] for s in students}
print(score_dic)
#7. 默认值填充：为缺失键设默认值
keys = ['a','b','c','d']
default_value = 0
default_dic = {key:0 for key in keys}
print(default_dic)

##集合推导式
setnew = {i**3 for i in (1,2,3)}
print(setnew)

a = {s for s in 'abracadabra' if s not in 'abc'}
print(a)

#1. 从列表去重并平方
number = [1,2,2,3,4,4,4,5,6,7,8,8]
squarter = {x**2 for x in number if x%2 == 0}
print(squarter)
#2. 提取字符串中所有唯一字符（转小写）
word = 'Hello WORLD!@@'
unique_chars = {char.lower() for char in word if char.isalpha()}
print(unique_chars)
#3. 求两个列表的交集（用推导式实现）
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = {x for x in list1 if x in list2}
intersection1 = set(list1)&set(list2)
print(intersection)
print(intersection1)
#4. 筛选满足条件的偶数并去重
nums = [10, 15, 20, 25, 30, 20, 10]
even_nums = {x for x in nums if x%2 == 0}
print(even_nums)
#5. 生成一组唯一的随机数（结合 random）
import random
random_set = {random.randint(1, 10) for _ in range(20)}#_ 是一个惯用变量名，表示“我不关心这个变量的值，只是用来循环”。
print(random_set)
# 输出示例: {1, 2, 4, 5, 7, 9, 10}  ← 最多10个不同数，自动去重
#6. 从嵌套列表中提取所有唯一元素
matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
flat_unique = {num for row in matrix for num in row}
print(f'flat_unique: {flat_unique}')

##元组推导式（生成器表达式）
a = tuple(x for x in range(1,10))
print(a)

#1. 基本形式：平方数生成器
gen = (x**2 for x in range(1, 5))
print(gen)        # <generator object <genexpr> at 0x...>
print(list(gen))  # [1, 4, 9, 16] —— 转成列表才能看到内容
#2. 带条件过滤：偶数的立方
even_cube = (x**3 for x in range(1,11) if x%2 == 0)
print(list(even_cube))
print(list(even_cube)) #生成器只能遍历一次！再次 list(gen) 会得到空列表。
#3. 处理字符串：转大写并过滤长度
words = ['apple', 'bat', 'cat', 'dog']
short_upper = (word.upper() for word in words if len(word) <= 3)
print(list(short_upper))
# 输出: ['BAT', 'CAT', 'DOG']
#4. 节省内存：处理大范围数据（推荐场景！）
hug_gen = (x for x in range(1_000_000))
total = sum(hug_gen)
print (total)
#5. 嵌套生成器表达式（谨慎使用）
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = (x for row in matrix for x in row)
print(tuple(flattened))
#6. 和函数结合：直接传入生成器（高效！）
num = [1,2,3,4,5]
total = sum(x for x in num)
print(total)