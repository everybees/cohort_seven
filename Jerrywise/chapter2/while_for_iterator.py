# for the_char in 'hi moo':
#     print(the_char)

# numbers = int(input("Enter a number"))
#
# divisor = 1
# sum_of_didvisor = 0
# while divisor < numbers:
#     if numbers % divisor == 0:
#         sum_of_didvisor = sum_of_didvisor + divisor
#     divisor = divisor + 1
#
# if numbers == sum_of_didvisor:
#     print(numbers, "is perfect")
# else:
#     print(numbers, "is not perfect")


numbers = int(input("Enter a number"))

number = 2
sum_of_didvisor = 0
while number < numbers:
    if numbers % number == 0:
        sum_of_didvisor = sum_of_didvisor + number
    number = number + 1

if numbers == sum_of_didvisor:
    print(numbers, "is perfect")
else:
    print(numbers, "is not perfect")