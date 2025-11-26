#. 基本语法
#with 表达式 as 变量:
    # 使用变量的代码块

#1. 常见用途：文件操作
with open('Python3 with/example.txt', 'r') as f: #使用 with 避免了忘记关闭文件或异常导致未关闭的问题。

    content = f.read()
    print(content)
# 文件在这里自动关闭，即使发生异常也会关闭
print('文件已关闭')

f = open('Python3 with/example.txt', 'r') 
try:
    content = f.read()
    print(content)
finally:
    f.close()

# 同时打开多个文件
with open('Python3 with/input.txt', 'r') as infile, open('Python3 with/output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())

#2. 数据库连接
import sqlite3

with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    print(results)

#3. 线程锁
import threading

lock = threading.Lock()

with lock:
    # 临界区代码
    print("这段代码是线程安全的")

import decimal


#4. 临时修改系统状态
with decimal.localcontext() as ctx:
    ctx.prec = 42  # 临时设置高精度
    # 执行高精度计算
# 精度恢复原设置