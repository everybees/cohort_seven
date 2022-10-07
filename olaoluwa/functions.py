from olaoluwa.building import Building

building = {
    "cohort": [
        {
            "name": "",
            "natives": [
                {
                    "scn": "",
                    "first_Name": "",
                    "last_name": "",
                    "sex": "Male"
                }
            ]
        }
    ]

}

def create_building(name, description, cohorts):
    building = Building(name, description, cohorts)
    return building

def