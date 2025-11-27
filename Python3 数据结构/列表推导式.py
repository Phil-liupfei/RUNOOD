#列表推导式
vec = [2,4,6]
new_vec = [x*2 for x in vec]
print(new_vec)   # [4, 8, 12]
new_vec1 = [[x,x**2] for x in vec]
print(new_vec1)  # [[2, 4], [4, 16], [6, 36]]
# 列表推导式也可以用在条件语句中，比如：
vec = [2,4,6,8,10]
new_vec = [x for x in vec if x%2 == 0]
print(new_vec)   # [2, 4, 6, 8, 10]  保留偶数   

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
new_fruit = [fruit.strip() for fruit in freshfruit]
print(new_fruit)  # ['banana', 'loganberry', 'passion fruit']  去除空格 

vec1 = [2,4,6]
vec2 = [4,3,-9]     
new_vec = [x*y for x in vec1 for y in vec2]
print(new_vec)  # [8, 6, -18, 12, 12, -54, 16, 16, -81]  笛卡尔积   
new_vec1 = [x+y for x in vec1 for y in vec2]
print(new_vec1)  # [6, 5, -7, 7, 5, -3, 9, 7, -5]  元素相加         
new_vec2 = [str(round(355/113,i)) for i in range(1,6)] # 生成器表达式
print(new_vec2)  # ['3.142', '3.1416', '3.14159', '3.141593', '3.1415926']  计算圆周率

A1 = [1,2,3]
A2 = [4,5,6]
A3 = [7,8,9]
new_A = [[A1[i],A2[i],A3[i]] for i in range(len(A1))]
print(new_A)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]  列出三维列表
new_vec = [A1,A2,A3]
print(new_vec)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  列表嵌套
matrix = [
    [1,2,3,4],
    [5,6,7,8],    
    [9,10,11,12]
]    

new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]  转置矩阵