import sqlite3

# 第一步：确保表存在
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT
        )
    ''')
    conn.commit()  # 虽然 with 会自动 commit，但显式写更清晰（可选）

# 第二步：插入一些测试数据（可选）
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("张三", "zhangsan@example.com"))
    # 注意：with 语句会自动 commit

# 第三步：现在可以安全查询了
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    print(results)