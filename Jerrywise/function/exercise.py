# Question 1




def maximium_number_of_three():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    third_number = int(input("Enter third number: "))
    if first_number > second_number and first_number > third_number:
        return first_number
    elif second_number > third_number and second_number > first_number:
        return second_number
    else:
        return third_number


# execise 2
def sum_number_in_lists():
    list =  z[]
    number = int(input("Enter number"))
    total = 0
    for numbers in number:
        total += numbers
        return total

# execise 3
def multiply_number_in_lists():
    number = int(input("Enter number"))
    total = 1
    for numbers in number:
        total *= numbers
    return total

#exercise 4
def word_reverse():
    word = input("Enter the word you want to reverse")
    reverse_word = ''
    index = len(word)
    while index > 0:
        reverse_word += word[index - 1]
        index = index-1
    return reverse_word

#exercise 5
# def calculating_factorial_of_number():
# number = int(input("Input a number to compute the factiorial : "))
#     if number == 0:
#             return 1
#         else:
#             return number * factorial(number - 1)


# #exercise 6
# def calculate_range_in_numbers(number):
#     if number in range(3,9):
#         print("%s the number is in range" %str(number))
#     else:
#         print("this number is not in range")
#
# #exercise 7





