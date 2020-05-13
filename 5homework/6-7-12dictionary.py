#!/usr/bin/python
print("###6-7###")
user_1 = {'first_name': 'djan', 'last_name': 'buffon', 'age': '40', 'city': 'parma'}
user_2 = {'first_name': 'cristiano', 'last_name': 'ronaldo', 'age': '33', 'city': 'lisabon'}
user_3 = {'first_name': 'alisыandro', 'last_name': 'del piero', 'age': '44', 'city': 'torin'}
users = [user_1, user_2, user_3]
for x in users :
    print(x)
print("###6-8###")
jeki = {'animals': 'dog', 'color': 'red', 'owner': 'masha'}
scotch = {'animals': 'cat', 'color': 'grey', 'owner': 'sergey'}
pets = [scotch, jeki]
# for pet in pets[:1]:
for pet in pets:
    # print (pet)
    for x, y in pet.items():
        print(y)
        print(x)
print("###6-9###")
numbers = {
    'masha': ['1', '2'],
    'vova': ['3', '5'],
    'petya': ['4', '6'],
    }
for name, number in numbers.items():
    print("\n" + name.title() + "favorite numbers is" )
    for x in number:
        print(x)
print("###6-10###")
citys = {
    'minsk': {
        'country': 'belarus',
        'population':'2m',
        'fact': 'the capitals Belarus'
        },
    'torin': {
        'country': 'italy',
        'population': '3m',
        'fact': 'juventus',
        },
    }

for city, city_info in citys.items():
    print("\ncity: " + city)
    print(city_info)
    city_fact = city_info['country'] + " " + city_info['population'] + " " + city_info['fact']
    print(city_fact)