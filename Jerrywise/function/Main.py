import builtins
from functions.cohort_records import Building, Cohort, Native
from functions import cohort_records
if __name__ == "__main__":
    main_building = cohort_records.Building("Semicolon Village", "312 Herbert Macaulay, Sabo, Yaba")
    native_1 = cohort_records.Native("1", "Sam", "Paul", "M")
    native_2 = cohort_records.Native("2", "Grace", "Favour", "F")
    cohort_1 = cohort_records.Cohort("Cohort One Natives")
    cohort_1.cohort_natives.append(native_1.__str__())
    cohort_1.cohort_natives.append(native_2.__str__())
    main_building.cohorts.append(cohort_1.__str__())

    native_2_1 = cohort_records.Native("1", "Victor", "Olamide", "M")
    native_2_2 = cohort_records.Native("2", "Tosin", "Akinnusi", "M")
    cohort_2 = cohort_records.Cohort("Cohort Two Natives")
    cohort_2.cohort_natives.append(native_2_1.__str__())
    cohort_2.cohort_natives.append(native_2_2.__str__())
    main_building.cohorts.append(cohort_2.__str__())

    native_3_1 = cohort_records.Native("1", "Precious", "Joy", "F")
    native_3_2 = cohort_records.Native("2", "Ahmad", "Ajala", "M")
    cohort_3 = cohort_records.Cohort("Cohort Three Natives")
    cohort_3.cohort_natives.append(native_2_1.__str__())
    cohort_3.cohort_natives.append(native_3_2.__str__())
    main_building.cohorts.append(cohort_3.__str__())

    native_4_1 = cohort_records.Native("1", "Muqtar", "Adetunji", "M")
    native_4_2 = cohort_records.Native("2", "Dami", "Omolori", "F")
    cohort_4 = cohort_records.Cohort("Cohort Four Natives")
    cohort_4.cohort_natives.append(native_4_1.__str__())
    cohort_4.cohort_natives.append(native_4_2.__str__())
    main_building.cohorts.append(cohort_4.__str__())

    print(main_building)
    global_container = []
    number_of_building = int(input("How many buildings do you want to generate: "))
    for i in range(number_of_building):
        name_of_building = input("Enter the name for building " + str(i+1) + ": ")
        description = input("Enter the address for " + name_of_building + ": ")
        building = Building(name_of_building, description)
        number_of_cohorts = int(input("Enter the number of cohorts in " + name_of_building + ": "))
        for i in range(number_of_cohorts):
            name_of_cohort = input("Enter name for cohort "+ str(i+1)+ ": " )
            cohort = Cohort(name_of_cohort)
            number_of_natives = int(input("Enter the number of natives in " + name_of_cohort + ": "))
            for i in range(number_of_natives):
                id_number = input("Enter id number for native " + str(i+1) + " in " + name_of_cohort +": ")
                first_name = input("Enter the firstname: ")
                last_name = input("Enter the lastname: ")
                gender = input("Enter gender type: ")
                native = Native(id_number, first_name, last_name, gender)
                cohort.cohort_natives.append(native.__str__())
            building.cohorts.append(cohort.__str__())
        global_container.append(building.__str__())

    for building in global_container:
        print(building)
