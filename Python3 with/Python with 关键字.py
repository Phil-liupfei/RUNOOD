with open('d:/Python_Learning/RUNOOD/Python3 with/example.txt', 'r') as f:
    content = f.read()
    print(content)
# 文件在这里自动关闭，即使发生异常也会关闭
