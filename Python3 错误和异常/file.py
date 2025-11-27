import os
topics = ['F?1','F:2','F<3']
#os.makedirs('temp/test')
def sanitize_folder_name(name):
    illegal_chars = '<>:"|?*'
    for char in illegal_chars:
        name = name.replace(char,'_')
    name = name.replace('/', '_').replace('\\', '_')
    return name.strip()
print(sanitize_folder_name('a<r>t:y"t|w?q*o'))
folder = 'temp/test'
for topic in topics:
    topic = sanitize_folder_name(topic)
    path = os.path.join(folder,topic)
    os.makedirs(path,exist_ok = True)
    print(f'Folder {path} was created !')
