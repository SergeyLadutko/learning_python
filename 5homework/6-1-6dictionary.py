#!/usr/bin/python
print("###6-1###")
human = {'first_name': 'ivanov', 'last_name': 'sergey', 'age': '24', 'city': 'minsk'}
print(human['first_name'])
print(human['last_name'])
print(human['age'])
print(human['city'])
print("*****")
for x, y in human.items():
    print(x)
    print(y)
print("###6-2###")    
numbers = {'masha': '1', 'vova': '2', 'sasha': '3'}
print("Masha favorite numbers " + numbers['masha'].title())
print("Sasha favorite numbers " + numbers['sasha'].title())
print("Vova favorite numbers " + numbers['vova'].title())
print("###6-4###")
name = {
    'devops': 'DevOps is a set of practices that combines software development (Dev) and information-technology operations (Ops) which aims to shorten the systems development life cycle and provide continuous delivery with high software quality',
    'docker': 'is a set of platform as a service (PaaS) products that uses OS-level virtualization to deliver software in packages called containers.',
    'linux': 'is a family of open source Unix-like operating systems based on the Linux kernel',
    }
for key, value in name.items():
    print("\nDEVOPS  " + key)
    print(value)
print("###6-5###")
rivers = {'neman': 'belarus', 'nile': 'egipt', 'visla': 'poland'}
for river, cauntry in rivers.items():
    print("\nIn this " + cauntry.title() + "a " + river.title() + " flows" )
print("###6-6###")
people = {
    'vasia' : 'c',
    'petia': 'c++',
    'vova': 'ruby',
    'sergey': 'python',
    }
peoples = ['vasia', 'petia', 'sergey', 'masha']
for name in people:
    print(name)
    if name in peoples:
        print("ok " + name.title())
    if name not in peoples:
        print("no " + name.title() + " in list" )