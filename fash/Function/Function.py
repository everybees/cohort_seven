from classTask import Building, Cohorts, Natives

building = {
    "name": "Semicolon Village",
    "description": "Growing Talent",
    "cohorts": [
        {
            "name": "Cohort One",
            "description": "These are the Alphas",
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
            },
        ]
        },
        {
            "name": "Cohort Two",
            "description": "These are the Alphas",
            "natives": [
                {
                    "scn": "001",
                    "first_name": "Han",
                    "last_name": "Tayo",
                    "sex": "Female"

                },
                {
                    "scn": "002",
                    "first_name": "ben",
                    "last_name": "kim",
                    "sex": "Male"

                },
                {
                    "scn": "003",
                    "first_name": "Funsho",
                    "last_name": "Teslim",
                    "sex": "Male"

                }
            ]
        }
    ]
}


def create_building(name, description, cohorts):
    building = Building(name, description, cohorts)
    return building


def create_cohort(name, description, natives):
    cohort = Cohort(name, description, natives)
    return cohort


def create_natives(scn, first_name, last_name, sex):
    native = Native(scn, first_name, last_name, sex)
    return native


def print_natives_data():
    print("Building Name:", building['name'])
    print("================================================================")
    print("Building Description:", building['description'])
    print("================================================================")
    print("Cohort Name:", building['cohorts'][0]['name'])
    print("================================================================")
    print("Cohort Description:", building['cohorts'][0]['description'])
    print("Scn No. \t First Name \t Last Name \t Sex")
    print("================================================================")
    for cohort in building["cohorts"]:
        print(cohort['name'])
        for native in cohort["natives"]:
            print(native['scn'] + "\t|\t"+
                  native['first_name'] + "\t|\t" +
                  native['last_name'] + "\t|\t" +
                  native['sex']
                  )
            print("===============================================================")


print_natives_data()


