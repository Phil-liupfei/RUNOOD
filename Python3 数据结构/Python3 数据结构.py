##Python3 数据结构
##列表
list1 = [1, 2, 3, 4, 5]
print(list1)
list1.append(6)
print(list1)
list1.extend([7, 8, 9]) # 合并两个列表
print(list1)
list1.insert(2, 10)
print(list1)
list1.remove(10)
print(list1)
list1.pop()
print(list1)
list1.clear()
print(list1)



list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
print(list1.count(3))
print(list1.index(3))
list1_copy = list1.copy()     # 复制列表    
print(list1_copy)

print('将列表当做栈使用')  
# 创建一个空栈
stack = []
print(stack)

# 压入(Push)操作
# 使用 append() 方法将元素添加到栈的顶端：
stack.append(1)
stack.append(2)
stack.append(3)
print(stack) # [1, 2, 3]

# 弹出(Pop)操作
# 使用 pop() 方法移除并返回栈顶元素：
top_element = stack.pop()
print(top_element) # 3
print(stack) # [1, 2]

# 查看栈顶元素(Peek/Top)
# 直接访问列表的最后一个元素(不移除)：
print(stack[-1]) # 2

# 检查是否为空(IsEmpty)
# 检查列表是否为空：
isempty = len(stack) == 0
print(isempty)


# 获取栈的大小(Size)
# 使用 len() 函数获取栈中元素的数量：
size = len(stack)
print(size) # 2


print('将列表当做队列使用')
# 创建一个空队列
queue = []
print(queue)

# 入队(Enqueue)操作
# 使用 append() 方法将元素添加到队列的尾端：
queue.append(1)
queue.append(2)
queue.append(3)
print(queue) # [1, 2, 3]

# 出队(Dequeue)操作
# 使用 pop(0) 方法移除并返回队列的第一个元素：
first_element = queue.pop(0)
print(first_element) # 1
print(queue) # [2, 3]

# 查看队列头元素(Peek/Front)
# 直接访问列表的第一个元素(不移除)：
print(queue[0]) # 2

# 检查是否为空(IsEmpty)
# 检查列表是否为空：
isempty = len(queue) == 0
print(isempty)

