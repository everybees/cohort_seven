from ozioma.building import class_task

if __name__ == "__main__":
    natives_1 = []
    natives_2 = []
    natives_3 = []

    native_1 = class_task.Native("Ozi", "Ozo", "SCN01", "F")

    native_2 = class_task.Native("Assi", "Iye", "SCN02", "M")

    native_3 = class_task.Native("Mata", "Joy", "SCN03", "M")
    natives_1.append(native_1)
    natives_1.append(native_2)
    natives_1.append(native_3)

    native_4 = class_task.Native("Seyi", "Ale", "SCN04", "F")
    native_5 = class_task.Native("Inno", "Alli", "SCN05", "M")
    native_6 = class_task.Native("Mono", "Bali", "SCN06", "M")
    natives_2.append(native_4)
    natives_2.append(native_5)
    natives_2.append(native_6)

    native_7 = class_task.Native("Esi", "Haru", "SCN07", "F")
    native_8 = class_task.Native("Sura", "Ipo", "SCN08", "M")
    native_9 = class_task.Native("Wena", "Yula", "SCN09", "M")
    natives_3.append(native_7)
    natives_3.append(native_8)
    natives_3.append(native_9)

    cohorts = []

    new_cohort_1 = class_task.Cohorts("1", natives_1, "First cohort.")
    new_cohort_2 = class_task.Cohorts("2", natives_2, "Second cohort.")
    new_cohort_3 = class_task.Cohorts("3", natives_3, "Third cohort.")

    cohorts.append(new_cohort_1)
    cohorts.append(new_cohort_2)
    cohorts.append(new_cohort_3)

    semicolon_building = class_task.Building("Semicolon", cohorts)
    print(semicolon_building.name)

    for me in semicolon_building.cohorts:
        if me.cohort_name == "1":
            print(me.cohort_name + ":")
            print("SCN  No.|   First name   |   Last name   |    Sex")
            for native in me.natives:
                print(native.native_id + "  |    " + native.first_name + "   |    " + native.last_name)
        elif me.cohort_name == "2":
            print(me.cohort_name + ":")
            print("SCN  No.|   First name   |   Last name   |    Sex")
            for native in me.natives:
                print(native.native_id + "  |    " + native.first_name + "   |    " + native.last_name)
        elif me.cohort_name == "3":
            print(me.cohort_name + ":")
            print("SCN  No.|   First name   |   Last name   |    Sex")
            for native in me.natives:
                print(native.native_id + "  |    " + native.first_name + "   |    " + native.last_name)




























# while True:
#     value = int(input('Enter number between 1 and 11: '))
#     if value == 1:
#         print('Finding the maximum of three numbers')
#         print(exercises.max_of_three_numbers())
#     elif value == 2:
#         print('Adding values in a list')
#         print(exercises.add_values())
#     elif value == 3:
#         print('Summing of numbers in a list')
#         print(exercises.sum_of_numbers_in_a_list())
#     elif value == 4:
#         print('Multiplying numbers in a list')
#         print(exercises.multiply_numbers_in_a_list())
#     elif value == 5:
#         print('Reversing a string')
#         print(exercises.reverse_a_string())
#     elif value == 6:
#         print('Finding the factorial of a number')
#         print(exercises.factorial_of_a_number())
#     elif value == 7:
#         print('Checking if a number is within a range of inputted numbers')
#         print(exercises.check_number_within_a_range())
#     elif value == 8:
#         print('Counting the number of upper and lower cases in a list')
#         print(exercises.check_upper_and_lowercase_in_sentence())
#     elif value == 9:
#         print('Creating a list of unique values from a larger list')
#         print(exercises.create_a_list_with_unique_elements_of_given_list())
#     elif value == 10:
#         print('Checking if a number is prime or not')
#         print(exercises.find_prime_number())
#     elif value == 11:
#         print('Printing even numbers in a list')
#         print(exercises.print_even_number_from_a_list())
#     elif value == -1:
#         print('Thank you for partaking in our game.')
#         break
