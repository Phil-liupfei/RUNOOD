class Dog:
    species = "狗"
    def __init__(self,name,age):
        self.name = name #这个狗的名字
        self.age = age #这个狗的年龄

    def bark(self): # 方法：狗的行为
        print(f'{self.name} says 汪汪！')

dog1 = Dog("小白",3)
dog2 = Dog("旺财",5)

dog1.bark()
dog2.bark()
print(dog1.species)
print(Dog.species)
Dog.species = "犬科动物" # 输出：犬科动物（所有实例都变了！）

print(dog1.species)
dog2.species = "家犬" #只改变本实例
print(dog1.species)
print(dog2.species)
