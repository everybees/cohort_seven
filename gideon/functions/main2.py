from giddy import Building
from giddy import Native
from giddy import Cohort

if __name__ =="__main__":
    print("Welcome!")
    print("="*20)
    building_name = input("Enter Building name: ")
    building_address = input("Enter Building address: ")
    main_building = Building(building_name, building_address)
    
    number_of_cohorts = int(input("Enter number of cohorts to create: "))

    for n in range(0, number_of_cohorts):
        cohort_name = input("Enter cohort name: ")
        cohort = Cohort(cohort_name)

        number_of_natives = int(input("Enter number of natives: "))
        for r in range(0, number_of_natives):
            native_id = input("Enter native id: ")
            native_first_name = input("Enter native first name: ")
            native_last_name = input("Enter native last name: ")
            native_sex = input("Enter native gender: ")

            native = Native(native_id, native_first_name, native_last_name, native_sex)

            cohort.cohort_natives.append(native.__str__())
        
        main_building.cohorts.append(cohort.__str__())


    print(main_building)
  