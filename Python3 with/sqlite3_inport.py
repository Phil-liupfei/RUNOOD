# 第三步：现在可以安全查询了
import sqlite3
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    print(results)

import threading

lock = threading.Lock()

with lock:
    # 临界区代码
    print("这段代码是线程安全的")