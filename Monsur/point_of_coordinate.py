
X = float(input("Enter value of X: "))
Y = float(input("Enter value of y: "))
if X == 0 and Y == 0:
    print("it's origin!")
elif (X == 0 and Y != 0) or (X != 0 and Y == 0):
    print("One of the coordinate is equal to zero")


# question 3
Index = float(input("Enter value of index: "))
if Index < 2:
    print("Analytic")
elif 2 < Index <= 3:
    print("Synthetic")
elif Index > 3:
    print("polysynthetic")

# question 4
number = int(input("Enter value of number: "))
if number < 0:
    print("negative")
elif number > 0:
    print("positive")
elif number == 0:
    print("zero")




