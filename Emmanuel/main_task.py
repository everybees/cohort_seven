from functions import class_excercise

if __name__== "__main__":


    def create_cohort():
        number_of_cohorts=int(input("how many cohorts do you want to create?\n"))
        for _ in range(number_of_cohorts):
            cohort_name = input("Enter cohort name\n")
            cohort_desc = input("Enter cohort description\n")
            new_cohort = class_excercise.Cohort(cohort_name, cohort_desc)
            building.cohorts.append(new_cohort)


    def create_native():
        number_of_natives=int(input("how many natives do you want to create?\n"))
        for _ in range(number_of_natives):
            first_name = input("Enter native first name\n")
            last_name = input("Enter native last name\n")
            sex = input("Enter native gender\n")
            native_id= input("Enter native id\n")
            new_native = class_excercise.Native(first_name, last_name, sex, native_id)
            building.cohorts.add_native_to_cohort(new_native)

    def display_building():
        for cohort in building.cohorts:
            print (cohort.name+":")
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                print(native.native_id +   "        |"     + native.first_name + "          |"  + native.last_name  + "         |" + native.sex+"\n")
            print("="*105 + "\n")

        response=input("Do you want to create a building?\n")
        if response == "yes":
            response= input("Enter building name\n")
            building = class_excercise.Building(response)
      
        response =int(input("""
                1-> create cohort
                2-> create native
                3-> exit
        """))

        if response == 1:
             create_cohort()
        response=input("create natives?")   
        if response=="yes":
            create_native()    
        elif response == 2:
            create_native()
        else:
         display_building()
    display_building()


