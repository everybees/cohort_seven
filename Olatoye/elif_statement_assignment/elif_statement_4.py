def number_state(number):
	if number > 0:
		print("Positive")
	elif number < 0:
		print("Negative")
	else:
		print("Zero")
		
print("Enter a number")
number_state(int(input()))

