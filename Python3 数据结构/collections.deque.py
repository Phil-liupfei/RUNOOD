#使用 collections.deque 实现队列
import collections

# 创建队列
queue = collections.deque()  # 空队列

# 入队  
queue.append(1)  # 入队元素 1
queue.append(2)  # 入队元素 2
queue.append(3)  # 入队元素 3

# 出队  
print(queue.popleft())  # 输出 1
print(queue.popleft())  # 输出 2
print(queue.popleft())  # 输出 3

# 输出结果：    
# 1  
# 2  
# 3  

# 队列为空  
print(queue)  # 输出 deque([]) # 空队列
# 入队  
queue.append(4)  # 入队元素 4
queue.append(5)  # 入队元素 5   
# 出队  
print(queue.popleft())  # 输出 4
print(queue.popleft())  # 输出 5
# 队列为空  
print(queue)  # 输出 deque([]) # 空队列
# 队列的其他操作  
print(len(queue))  # 输出 0  
queue.append(6)  # 入队元素 6  
queue.append(7)  # 入队元素 7  
print(queue.pop())  # 输出 7  
print(queue.pop())  # 输出 6  
print(queue)  # 输出 deque([]) # 空队列 

# 向队尾添加元素
queue.append('a')
queue.append('b')
queue.append('c')

# 从队首移除元素
first_element = queue.popleft()
print("移除的元素:", first_element)  # 输出: 移除的元素: a
print("队列状态:", queue)            # 输出: 队列状态: deque(['b', 'c'])

# 查看队首元素（不移除）
front_element = queue[0]
print("队首元素:", front_element)    # 输出: 队首元素: b

# 检查队列是否为空
is_empty = len(queue) == 0
print("队列是否为空:", is_empty)     # 输出: 队列是否为空: False

# 获取队列大小
size = len(queue)
print("队列大小:", size)            # 输出: 队列大小: 2