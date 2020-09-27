password = '123456'
i = 3
while True:
	pwd = input('password:')
	if pwd == password:
		print('success')
		break
	else:
		i = i - 1
		print('Error' , i, 'chances left')
		if i == 0:
			break