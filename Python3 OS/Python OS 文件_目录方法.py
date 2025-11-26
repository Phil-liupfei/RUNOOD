#ython OS 文件/目录方法
import os

os_name = os.name #获取当前操作系统类型，nt 表示Windows，posix 表示类Unix系统。
print(os_name) 

os_cwd = os.getcwd() # Get the current working directory (CWD) 
print(os_cwd)

d = dir(os) #查看os下的所有函数
for i in d:
    print ("os下面的函数：",i)
d = dir(os.path)
for i in d:
    print("os.path下面的函数：",i)

#一、路径操作（Path Operations）
#获取当前工作目录（Current Working Directory）。
os_cwd = os.getcwd() #获取当前工作目录（Current Working Directory）。
print(os_cwd)

os.chdir('D:\Python_Learning') #改变当前工作目录。
os.chdir('../') 
print(os.getcwd())
os.chdir('D:\Python_Learning\RUNOOD')

print(os.path.abspath('README.MD'))#os.path.abspath(path) 
print(os.path.abspath('Python OS 文件_目录方法'))

print(os.path.join('folder','sub','file.txt')) #os.path.join(path, *paths) 智能拼接路径（跨平台兼容）。

print(os.path.basename('/home/user/file.txt')) #os.path.basename(path) 返回路径中的文件名部分。
print(os.path.basename('D:/Python_Learning/RUNOOD/Python3 OS/file.py')) #os.path.basename(path) 返回路径中的文件名部分。

#os.path.dirname(path)
print(os.path.dirname('/home/user/file.txt')) #os.path.dirname(path) 返回路径中的文件名部分。
print(os.path.dirname('D:/Python_Learning/RUNOOD/Python3 OS/file.py')) #os.path.dirname(path) 返回路径中的文件名部分。
#os.path.split(path)
print(os.path.split('/home/user/file.txt')) #将路径拆分为 (目录, 文件名) 元组。
#os.path.splitext
print(os.path.splitext('/home/user/file.txt')) #分离文件名和扩展名。
#os.path.exists(path)
print(os.path.exists('/home/user/file.txt')) #判断路径是否存在。
print(os.path.exists('D:/Python_Learning/RUNOOD/Python3 OS/')) #判断路径是否存在。
#os.path.isfile(path) 判断是否为文件。
#os.path.isdir(path)判断是否为目录。
print(os.path.isfile('D:/Python_Learning/RUNOOD/Python3 OS/Python OS 文件_目录方法.py'))
print(os.path.isdir('D:/Python_Learning/RUNOOD/Python3 OS/'))
#os.path.islink(path) #判断是否为符号链接（软链接）。
print(os.path.islink('D:/Python_Learning/RUNOOD/Python3 OS/Python OS 文件_目录方法.py'))
print(os.path.islink('D:/Python_Learning/RUNOOD/Python3 OS/GitHub 零基础入门教程'))
#os.path.getsize(paht) 获取文件大小（字节）。
print(os.path.getsize('D:/Python_Learning/RUNOOD/Python3 OS/Python OS 文件_目录方法.py'))
#os.path.getatime(path) 获取文件最后修改时间（时间戳）。
import time
timeStamp = os.path.getatime('D:/Python_Learning/RUNOOD/Python3 OS/Python OS 文件_目录方法.py')
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
print(os.path.getatime('D:/Python_Learning/RUNOOD/Python3 OS/Python OS 文件_目录方法.py'))
#os.path.normpath(path) 规范化路径（如处理 .. 和 .）。
print(os.path.normpath('D:/Python_Learning/RUNOOD/Python3 OS/Python OS 文件_目录方法.py'))
print(os.path.normpath('C:\\Users\\.\\Documents'))


##