first_num = int(input('Введите первое число: \n'))
second_num = int(input('Введите второе число: \n'))
operator = input('Введите [+, -]: \n')

if operator == '+':
	result = first_num + second_num
elif operator == '-':
	result = first_num - second_num

print('{} {} {} = {}'.format(first_num, operator, second_num, result))