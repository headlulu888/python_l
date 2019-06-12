first_num = int(input('Введите первое число: \n'))
second_num = int(input('Введите второе число: \n'))

i = first_num - 1
while i <= second_num:
	if i % 5 == 0:
		print(i)
	i += 1