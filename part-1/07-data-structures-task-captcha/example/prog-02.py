'''
словарь
список
кортеж
строка
'''
d = {
	0: ('##','##','##','##'),
	1: ('.#','##','.#','.#')
}

dig = int(input())
print('\n'.join(d[dig]))
