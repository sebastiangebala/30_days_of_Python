def check_value(i):
	if isinstance(i, int):
		if i == 0:
			print('to jest zero koleś!')
		elif i >= 1 and i <= 10:
			print('między 1 a 10') 
		elif i >= 11 and i <= 99:
			print('dzięsiątki mamy')
		else:
			print('Łooooo Panie tosz to wielka liczba!')
	else:
		print('miała być liczba!')
		