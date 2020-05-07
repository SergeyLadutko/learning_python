#!/usr/bin/python
###4-10###
slice_list = ['juventus', 'playstation', 'telegram', 'bladborn']
for x in slice_list[:3]:
    print(x.title() + " My test slice")
print('##########################')
for x in slice_list[:3]:
    print(x.title() + " My test slice")
print('##########################')
for x in slice_list[-3:]:
    print(x.title() + " My test slice")
print('##########################')
###4-11###
print("########################4-11######################")
pizza_list = ['peperoni', 'diblo', '4chize']
friend_pizza_lista = pizza_list[:]
pizza_list.append('margrita')
friend_pizza_lista.append('test pizza')
print(friend_pizza_lista)
print(pizza_list)
###4-12###
print("########################4-12######################")
pizza_list = ['peperoni', 'diblo', '4chize']
friend_pizza_lista = pizza_list[:]
pizza_list.append('margrita')
friend_pizza_lista.append('test pizza')
print("my pizza".upper())
for x in pizza_list:
    print(x.title())
print("friend pizza".upper())
for x in friend_pizza_lista:
    print(x.upper())
print(friend_pizza_lista)
print(pizza_list)