from building import Building_OOP
building = {
    "name": "Semicolon Village",
    "description": "Growing Talent",
    "cohorts": [
        {
            "name": "Cohort One",
            "description": "These are the Alphas!",
            "natives": [
                {
                    "scn": "001",
                    "first_name": "Babyface",
                    "last_name": "Teju",
                    "sex": "Female"
                },
                {
                    "scn": "002",
                    "first_name": "Sam",
                    "last_name": "Tega",
                    "sex": "Male"
                }
            ]
        },
        {
            "name": "Cohort Two",
            "description": "",
            "natives": [
                {
                    "scn": "",
                    "first_name": "",
                    "last_name": "Tayo",
                    "sex": "Male"
                },
                {
                    "scn": "",
                    "first_name": "",
                    "last_name": "Kim",
                    "sex": "Female"
                },
                {
                    "scn": "",
                    "first_name": "",
                    "last_name": "Teslim",
                    "sex": "Male"
                }
            ]
        }
    ],
}


def create_building(name, description, cohorts):
    building = Building_OOP.Building(name, description, cohorts)
    return building

def create_cohort(name, description, natives):
    cohort = Building_OOP.Cohort(name, description, natives)
    return cohort

def create_natives(scn, first_name, last_name, sex):
    native = Building_OOP.Native(scn, first_name, last_name, sex)
    return native

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
def print_natives_data():
    print("Building Name: ",building['name'])
    print("Description: ", building['description'])
    print("=================================")
    print("Cohort Name: ", building['cohorts'][0]['name'])
    print("Cohort Description: ",building['cohorts'][0]['description'])
    print("SCN No. \t|First Name \t|Last Name \t|Sex")
    print("-------------------------------------------------------------------")
    for cohort in building['cohorts']:
        for native in cohort['natives']:
            print(native['scn'] + "\t|\t" + 
            native['first_name'] + "\t|\t" + 
            native['last_name'] + "\t|\t" +
            native['sex']
            )
            print("-------------------------------------------------------------------")


print_natives_data()
