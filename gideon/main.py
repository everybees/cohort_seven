# import chat_bot_1

# if __name__ == "__main__":
#     chat_bot_1.do_something()

# from gideon import chat_bot_1
# import chat_bot_1, calculator

# if __name__ == "__main__":
#     while True:
#         user_number = int(input("Enter a number: "))
#         if user_number > 10:
#             print("UNKNOWN COMMAND!!")
#             print("Exiting main...")
#             break
#         if 1 == user_number:
#             chat_bot_1.do_something()
#         elif 2 == user_number:
#             calculator.calculate()


# from functions import exercise
# if __name__ == "__main__":
#     print(exercise.max_of_three_numbers(a=220, b=300, c=90))

# from functions import exercise
# if __name__ == "__main__":
#     exercise.sum_of_numbers_in_a_list([2,6,4,4,3,1,2])

# from functions import exercise
# if __name__ == "__main__":
#     exercise.product_of_numbers_in_a_list()


# from functions import exercise
# if __name__ == "__main__":
#     exercise.reverse_print()

# from functions import exercise
# if __name__ == "__main__":
#     exercise.factorial(a=5)

# from functions import exercise
# if __name__ == "__main__":
#     exercise.num_in_range(a=5, x=2, y=10)

# from functions import exercise
# if __name__ == "__main__":
#     exercise.upper_lower_case()

# from functions import exercise
# if __name__ == "__main__":
#     exercise.unique_list()

# cohort_eight_natives = []

# import cohort_eight

# if __name__ == "__main__":
#     # create student
#     student_1 = cohort_eight.create_student("Tife", "Olanipekun", "tifepekun@gmail.com","08066778899", "male")
#     cohort_eight_natives.append(student_1)
#     student_2 = cohort_eight.create_student("Yetunde", "Boluwatife", "yetundebolu@gmail.com","08066778890", "female")
#     cohort_eight_natives.append(student_2)
#     student_3 = cohort_eight.create_student("Demola", "Adeniyi", "demolaniyi@gmail.com","08066778891", "male")
#     cohort_eight_natives.append(student_3)
#     student_4 = cohort_eight.create_student("John", "Oladeji", "johnola@gmail.com","08066778892", "male")
#     cohort_eight_natives.append(student_4)

#     student_1["courses"].append("java")
#     student_2["courses"].append("java")

#     for element in cohort_eight_natives:
#         if "java" not in element["courses"]:
#             element["courses"].append("java")

# print(cohort_eight_natives)
    # native = cohort_eight.Native("Tife", "Bolu")
    # print(native.first_name, native.last_name)
# import second_example

# if __name__ == "__main__":
#     next_of_kin=[]
#     next_of_kin1 = second_example.create_next_of_kin("quin","ajohne","07062783014","female","wife")
#     next_of_kin.append(next_of_kin1)
#     second_example.register_native_to_cohort("segun", "john","male","08024355419","sleepyjohn@gmail.com",next_of_kin)
#     print(second_example.cohort_eight[0].next_of_kin[0].first_name)
import class_task

if __name__ == "__main__":
    native1 = []
    student1 = class_task.Natives("Yetunde", "Olasehinde", "female", "SCN No1")
    native1.append(student1)
    student2 = class_task.Natives("Kareem", "Monsur", "male", "SCN No2")
    native1.append(student2)
    student3 = class_task.Natives("Lantana", "Tijani", "female", "SCN No3")
    native1.append(student3)
    student4 = class_task.Natives("Femi", "Oladeji", "male", "SCN No4")
    native1.append(student4)


    native2 = []
    student5 = class_task.Natives("Emmanuel", "Olorunishola", "male", "SCN No1")
    native2.append(student5)
    student6 = class_task.Natives("Ozioma", "Okoroafor", "female", "SCN No2")
    native2.append(student6)
    student7 = class_task.Natives("Damilola", "Omolori", "female", "SCN No3")
    native2.append(student7)
    student8 = class_task.Natives("Pastor-John", "Oladeji", "male", "SCN No4")
    native2.append(student8)

    native3 = []
    student9 = class_task.Natives("Tife", "Olanipekun", "male", "SCN No1")
    native3.append(student9)
    student10 = class_task.Natives("Adesuwa", "Odomela", "female", "SCN No2")
    native3.append(student10)
    student11 = class_task.Natives("Demola", "Adeniyi", "male", "SCN No3")
    native3.append(student11)
    student12 = class_task.Natives("Kimberly", "Oketope", "female", "SCN No4")
    native3.append(student12)

    native4 = []
    student13 = class_task.Natives("Goodnews", "Ozichukwu", "female", "SCN No1")
    native4.append(student13)
    student14 = class_task.Natives("Olatoye", "Daramola", "male", "SCN No2")
    native4.append(student14)
    student15 = class_task.Natives("Precious", "Onyeokwu", "female", "SCN No3")
    native4.append(student15)
    student16 = class_task.Natives("Segun", "MacManuel-Acme", "male", "SCN No4")
    native4.append(student16)




    cohorts = []
    cohort_one = class_task.Cohort("Cohort One", "Phoenix: Na Dem", native1)
    cohorts.append(cohort_one)
    cohort_two = class_task.Cohort("Cohort Two", "Sages: Sachet Sense", native2)
    cohorts.append(cohort_two)
    cohort_three = class_task.Cohort("Cohort Three", "Hoodlums: According to their name..", native3)
    cohorts.append(cohort_three)
    cohort_four = class_task.Cohort("Cohort Four", "Acme: Question Sir, primarily..", native4)
    cohorts.append(cohort_four)

    
    # building = class_task.Building("Building Name: Semicolon Village", cohorts)
    # print("=" * 35)
    # print(building.building_name)
    # print("=" * 35)
    # print()




    # print("SCN No.     ||    FIRST NAME         ||   LAST NAME         ||   SEX")
    # print("=" * 78)

    
    # for cohort in building.cohorts:
    #     # for native in cohort.native:
    #     #     print(native.id + "     |        " +native.first_name + "      |       " +native.last_name + "     |       " + native.sex)
    #     #     print("------------------------------------------------------------------------------")
        
    #     if cohort.cohort_name == "Cohort One":
    #         print ("Cohort Name:",cohort.cohort_name)
    #         print(cohort.cohort_description)
    #         print("=" * 78)
    #         print("SCN No.     ||    FIRST NAME         ||   LAST NAME         ||   SEX")
    #         for native in cohort.native:
    #             print(native.id + "\t\t\t" +native.first_name + "\t\t" +native.last_name + "\t\t" + native.sex)
    #             print("------------------------------------------------------------------------------")
    #     elif cohort.cohort_name == "Cohort Two":
    #         print ("Cohort Name:",cohort.cohort_name)
    #         print(cohort.cohort_description)
    #         print("=" * 78)
    #         print("SCN No.     ||    FIRST NAME         ||   LAST NAME         ||   SEX")
    #         print("=" * 78)
    #         for native in cohort.native:
    #             print(native.id + "\t\t\t" +native.first_name + "\t\t" +native.last_name + "\t\t" + native.sex)
    #             print("------------------------------------------------------------------------------")
    #     elif cohort.cohort_name == "Cohort Three":
    #         print ("Cohort Name:", cohort.cohort_name)
    #         print(cohort.cohort_description)
    #         print("=" * 78)
    #         print("SCN No.     ||    FIRST NAME         ||   LAST NAME         ||   SEX")
    #         print("=" * 78)
    #         for native in cohort.native:
    #             print(native.id + "\t\t\t" +native.first_name + "\t\t" +native.last_name + "\t\t" + native.sex)
    #             print("------------------------------------------------------------------------------")
    #     else:
    #         print ("Cohort Name:",cohort.cohort_name)
    #         print(cohort.cohort_description)
    #         print("=" * 78)
    #         print("SCN No.     ||    FIRST NAME         ||   LAST NAME         ||   SEX")
    #         print("=" * 78)
    #         for native in cohort.native:
    #             print(native.id + "\t" + "|" + "\t" + native.first_name + "\t" + "|" + "\t" + native.last_name + "\t" + "|" + "\t" + native.sex)
    #             print("------------------------------------------------------------------------------")

        

    building = []
    number_of_buildings = int(input("How many buildings do nyou want to create: "))
    for a in range(number_of_buildings):
        name_of_building = (input("Enter building name: "))
        building = class_task.Building(name_of_building, cohorts)
        number_of_cohorts = int(input("Enter the no of cohorts in " + str(a+1)+ ": "))
        for a in range(number_of_cohorts):
            name_of_cohort = input("Enter name of cohort " + str(a+1) + ": ")
            description = input("Enter cohort desciption: ")
            cohort = class_task.Cohort(name_of_cohort, description, native)
            number_of_natives = int(input("Enter the number of natives in " + name_of_cohort + ":" ))
            for a in range(number_of_natives):
                id_number = input("Enter id number of native " + str(a+1) + " in " + name_of_cohort + ": ")
                first_name = input("Enrer First Name: ")
                last_name = input("Enter last name: ")
                gender = input("Enter gender: ")
                # native = class_task.Natives(id_number, first_name, last_name, gender)
                # cohort.native.append(native._first_name_, native._last_name_, native._id_, native._sex)
            building.cohorts.append(cohorts)
            # building.append(building.cohorts)

    for cohort in building.cohorts:
        for native in cohort.native:
            print(native)