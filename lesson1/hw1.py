import sys

if not sys.version_info.major == 3:
	input = raw_input

questions = {
	'В каком году закончится поддержка Python 2.7?': '2020',
	'Существуют ли в Python цыклы с пост-условием?': 'нет',
	'Как в Python обозночается истина?': 'True',
	'Какая функция в Python используется для вывода сообщения в консоль': 'print()',
	'К какому типу данных относится данное число: 3.14': 'float',
	'В каком году появился язык Python': '1991',
	'a=\'string\', b="string". Оличаются ли друг от друга перменные a и b': 'нет'
}

incorrect_answer = 0

for question in questions:
	x = True
	while x:
		try:
			if input(question + '\n') != questions[question]:
				incorrect_answer += 1
				raise(ValueError())
			else:
				x = False
		except ValueError:
			print('Неправильный ответ попробуйте еще раз!')
print('Вы выйграли! Неправильных ответов - {}'.format(incorrect_answer))