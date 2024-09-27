import builtins
import building_records
from building_records import Building, Cohort, Native
if __name__ == "__main__":
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



















# main_building = building_records.Building("Semicolon Africa", "312 albert macully way, Sabo Yaba")
    # native_1 = building_records.Native("1", "Kelvin", "Okoro", "M")
    # native_2 = building_records.Native("2", "Omolara", "Ayobami", "F")
    # cohort_1 = building_records.Cohort("Cohort One Natives")
    # cohort_1.cohort_natives.append(native_1.__str__())
    # cohort_1.cohort_natives.append(native_2.__str__())
    # main_building.cohorts.append(cohort_1.__str__())
    #
    # native_2_1 = building_records.Native("1", "Beatrice", "Adopisa", "F")
    # native_2_2 = building_records.Native("2", "Henry", "Ogehato", "M")
    # cohort_2 = building_records.Cohort("Cohort Two Natives")
    # cohort_2.cohort_natives.append(native_2_1.__str__())
    # cohort_2.cohort_natives.append(native_2_2.__str__())
    # main_building.cohorts.append(cohort_2.__str__())
    #
    # native_3_1 = building_records.Native("1", "Hamad", "Anjorin", "M")
    # native_3_2 = building_records.Native("2", "Femi", "Baderinwa", "F")
    # cohort_3 = building_records.Cohort("Cohort Three Natives")
    # cohort_3.cohort_natives.append(native_2_1.__str__())
    # cohort_3.cohort_natives.append(native_3_2.__str__())
    # main_building.cohorts.append(cohort_3.__str__())
    #
    # native_4_1 = building_records.Native("1", "Ayomide", "Atoki", "M")
    # native_4_2 = building_records.Native("2", "Adeola", "Adedayo", "F")
    # cohort_4 = building_records.Cohort("Cohort Four Natives")
    # cohort_4.cohort_natives.append(native_4_1.__str__())
    # cohort_4.cohort_natives.append(native_4_2.__str__())
    # main_building.cohorts.append(cohort_4.__str__())
    #
    # print(main_building)