'''
class Person():
    def __init__(self, name, age, hobby):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.hobby = hobby

    def introduce(self):
        print(f"{self.hello}, 저는 {self.age}살 {self.name}입니다")

jin = Person('진', 22, '운동')
jin.introduce()
print(f"이름 : {jin.name}")
print(f"나이 : {jin.age}")
print(f"취미 : {jin.hobby}")
'''

class Person:
    folder = []

    def add_files(self, file):
        self.folder.append(file)

jin = Person()
jin.add_files('txt')

kim = Person()
kim.add_files('img')

print(jin.folder)
print(kim.folder)

print('hi')

# git config --global user.name
# git config --global 