def elif_statement_1():
	A = int(input("Enter recommended minimum sleeping hours: "))
	B = int(input("Enter recommended maximum sleeping hours: "))
	
	while A >= B:
		print("\nThe Minimum cannot be more than the Maximum\n")
		A = int(input("Enter recommended minimum sleeping hours: "))
		B = int(input("Enter recommended maximum sleeping hours: "))

	H = int(input("Enter your sleeping hours: "))

	if H > B:
		print("Excess")
	elif H < A:
		print("Deficiency")
	elif A < H < B:
		print("Normal")
		
elif_statement_1()

