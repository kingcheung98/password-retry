password = '123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('password:')
	if pwd == password:
		print('success')
		break
	else:
		print('Error')
		if i > 0:
			print( i, 'chances left')
		else:
			print('no more chance')
		