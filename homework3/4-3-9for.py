#!/usr/bin/python
###4-3###
numbers_list = list(range(1,21))
print(numbers_list)
###4-4###
numbers_list_second = list(range(1,1000001))
# for number in numbers_list_second:
#    print(number)
#print(numbers_list_second)
###4-5###
numbers_min = min(numbers_list_second)
print(numbers_min)
numbers_max = max(numbers_list_second)
print(numbers_max)
number_sum = sum(numbers_list_second)
print(number_sum)
###4-6###
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)
###4-7###
number_3 = list(range(0,31,3))
for number in number_3:
    print(number)
###4-8###
list_number = list(range(1,11))
for x in list_number:
    print(x**3)
###4-9###
kube_list = [value**3 for value in range(1,11)]
print(kube_list)

