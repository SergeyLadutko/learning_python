#!/usr/bin/python
print("###5-8-9###")
# admin = ['masha', 'jeki', 'scotch', 'sergey', 'devops' ]
# if admin:
#     print("Enter your name:")
#     x = input()
#     if x not in admin:
#         print(x.title() + " no admin")
#     else:
#         print("Hello " + x)
# else :
#     print('user admin not ctreate')
print("###5-10###")   
current_users = ['masha', 'jeki', 'scotch', 'sergey', 'devops' ]
new_users = ['masha', 'jeki', 'vasi', 'vova', 'Sergey']
for new_user in new_users:
    if  new_user.lower() in current_users:
        print(new_user + " A user with the same name exists.")
    else:
        print("new user " + new_user + " create")    
print("5-11")
numbers_list = list(range(1,10))
for x in numbers_list:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")   
    elif x == 3:
        print(str(x) + "rd")
    elif x >=4 and x < 10:
        print(str(x) + "th")
print(numbers_list)
