# first task
# list = [10, 12, 232, 94, 1, 77, 4]
# print(sorted(list))

# second task
# dict = {
# 	1: 'hello',
# 	2: 'world',
# 	6: 'testing_value',
# 	10: 'None',
# 	3: 'last_value'
# }

# for key, value in dict.items():
# 	print('Key is: {} - Value is: {}'.format(key, value))

# third task
# tuple = (1.4, 2.32, 10.1, 23.3, 50.4)
# print('Максимальное значение = ', max(tuple))
# print('Максимальное значение = ', min(tuple))

# fourth task
# fourth = ['Earth', 'Moscow', 'Python']
# string_from_list = '-'.join(fourth)
# print(type(string_from_list))
# print('Это на наш массив \n', fourth)
# print('Это строка из него: ', string_from_list)

# fifth task
# some_string = '/bin:/usr/bin:/usr/local/bin'
# data = some_string.split(':')
# print(data)

# sixth task
# print('Числа которые делятся на 7: ')
# str = ''

# for item in range(1, 100):
# 	if item % 7 == 0:
# 		str += '{}, '.format(item)
# # print(str[:-2])
# # or
# print(str.rstrip(', '))

# seven task
# matrix = [
# 	[1, 33, 2.5],
# 	[54, 103, 3],
# 	[97, 232, 4],
# 	[41, 14, 5.5]
# ]

# a = []
# b = []
# c = []

# for row in matrix:
# 	print(row)

# for col in matrix:
# 	a.append(col[0])
# 	b.append(col[1])
# 	c.append(col[2])

# print('First col is: ', a)
# print('Second col is: ', b)
# print('Third col is: ', c)

# eighth task
# list = ['hello', 123, None, True, 2.123]
# print('Это список:', list)

# for item in list:
# 	print('Индекс = ', list.index(item), ', Значение = ', item)

# ninth task
# list = ['to-delete', 123, None, True, 'to-delete', 1.22, 54, 'to-delete']
# print(list)

# for item in list:
# 	if item == 'to-delete':
# 		list.remove(item)
# print(list)

# tenth task
# num = 10
# while num > 0:
# 	print(num)
# 	num -= 1