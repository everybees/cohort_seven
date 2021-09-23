# from Olatoye.new_specials import chatbot, calculator
from Olatoye.functions import exercise


def function_caller():
    number = input("Enter your question number: ")

    func_dict = {
        "1": [exercise.max_of_three_numbers()],
        "2": [exercise.sum_of_numbers()],
        "3": [exercise.multiple_of_numbers()],
        "4": [exercise.reverse_string()],
        "5": [exercise.factorial()],
        "6": [exercise.number_in_range()],
        "7": [exercise.upper_and_lower()],
        "8": [exercise.unique_list_item()],
        "9": [exercise.prime_number()],
        "10": [exercise.even_number_from()],
        "11": [exercise.perfect_number()],
        "12": [exercise.palindrome()],
        "15": [exercise.hyphen_separator()]
    }

    for key in func_dict:
        if key in number:
            print(func_dict[key])
    # for key, value in func_dict.items():
    #     if key == number:
    #         # print(f"{key}\n{value.__doc__}")
    #         print(value)
    #     else:
    #         print("Sorry, number not in questions list...")


if __name__ == "__main__":
    # userInput = int(input())
    # if userInput == 1:
    #     calculator.calculator()
    # elif userInput == 2:
    #     chatbot.chatbot()
    function_caller()
