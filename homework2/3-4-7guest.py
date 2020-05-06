#!/usr/bin/python
###3-4###
guest = ['vitaliy', 'vova', 'masha']
message = "Hi go to me please " + guest[0].title()
print(message)
message = "Hi go to me please " + guest[1].title()
print(message)
message = "Hi go to me please " + guest[2].title()
print(message)
###3-5###
new_message = "sorry i can't come to you " + guest[0].title()
# del guest[0]
# print(guest)
new_guest_list = guest.pop(0).title()
print(new_guest_list)
new_person = "karolina"
message = "Hi go to me please " + new_person.title()
print(message)
guest.append(new_person)
print(guest)
###3-6###
guest.insert(0, 'jana')
guest.insert(-1, 'kolia')
print(guest)
###3-5###
print("Only two")
print(guest)
guest.pop(0)
print(guest)
guest.pop(0)
print(guest)
guest.pop(0)
guest.remove('kolia')
guest.remove('karolina')
print(guest)