import os
##二、目录与文件操作
#os.listdir(path='.')
print(os.listdir('.') )#列出指定目录下的所有文件和子目录。
dir = os.listdir('.') #列出指定目录下的所有文件和子目录。
for file in dir:
    print(file)
#os.mkdir(path, mode=0o777)
os.mkdir('new_folder') #创建目录。
print('new_folder was created')
os.rmdir('new_folder') #删除目录。
print('new_folder was removed')
os.makedirs('parent_older/child_folder') #递归创建多级目录。
print('parent_older/child_folder was created')
os.removedirs('parent_older/child_folder') #递归删除多级目录。
print('parent_older/child_folder was removed')


file = open("old_name.txt", "w")
file.close()
print('old_name.txt was created')
os.rename('old_name.txt', 'new_name.txt') #重命名文件或目录。
print('old_name.txt was renamed to new_name.txt')

os.remove('new_name.txt') #删除文件。
print('new_name.txt was removed')
