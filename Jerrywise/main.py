# import Chat_Bot
# import Calculator
from function import exercise

if __name__ == "__main__":
    print("""
    * please enter any of the option to perform a certain task or operation
    1.maximium_number_of_three.
    2.sum_number_in_lists.
    3.multiply_number_in_lists.
    4.word_reverse.
    5.calculating factorial of number.
    6.calculate_range_in_numbers.
    7.
    8.
    """)
    while True:
        user_input = int(input("choose any of the number between 1 and 10 to carry."))
        if user_input == 1:
            print(exercise.maximium_number_of_three())
        elif user_input == 2:
            print(exercise.sum_number_in_lists())





























# function = input("enter number for ")
#     number = int(input("enter a number: "))
#     if number == 1:
#         Chat_Bot.do_something()
#     else:
#         print("please enter 1")
#
#     Calculator.calculate_Something()









