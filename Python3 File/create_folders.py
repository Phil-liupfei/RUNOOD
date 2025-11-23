import os

# 所有要创建的文件夹名称（直接复制你提供的列表）
topics = [
    "Python3 基础语法",
    "Python3 基本数据类型",
    "Python3 数据类型转换",
    "Python3 解释器",
    "Python3 注释",
    "Python3 运算符",
    "Python3 数字(Number)",
    "Python3 字符串",
    "Python3 列表",
    "Python3 元组",
    "Python3 字典",
    "Python3 集合",
    "Python3 条件控制",
    "Python3 循环语句",
    "Python3 编程第一步",
    "Python3 推导式",
    "Python3 迭代器与生成器",
    "Python3 with",
    "Python3 函数",
    "Python3 lambda",
    "Python3 装饰器",
    "Python3 数据结构",
    "Python3 模块",
    "Python __name__",
    "Python3 输入和输出",
    "Python3 File",
    "Python3 OS",
    "Python3 错误和异常",
    "Python3 面向对象",
    "Python3 命名空间/作用域",
    "Python 虚拟环境的创建",
    "Python 类型注解",
    "Python3 标准库概览",
    "Python3 实例",
    "Python 测验"
]

# ⚠️ 修改这里：指定你要创建文件夹的根目录（用正斜杠 / 或双反斜杠 \\）
base_dir = "D:/Python_Learning"  # 示例路径，请按需修改！

# 自动清理文件夹名中的非法字符（Windows 不允许的字符）
def sanitize_folder_name(name):
    # Windows 禁止的字符：< > : " | ? *
    illegal_chars = '<>:"|?*'
    for char in illegal_chars:
        name = name.replace(char, '_')
    # 替换斜杠（虽然你的列表里没有，但保险起见）
    name = name.replace('/', '_').replace('\\', '_')
    return name.strip()

# 创建文件夹
for topic in topics:
    safe_name = sanitize_folder_name(topic)
    folder_path = os.path.join(base_dir, safe_name)
    try:
        os.makedirs(folder_path, exist_ok=True)  # exist_ok=True 避免报错已存在
        print(f"✅ 已创建: {safe_name}")
    except Exception as e:
        print(f"❌ 创建失败: {safe_name} - 错误: {e}")

print("\n🎉 所有文件夹创建完成！")