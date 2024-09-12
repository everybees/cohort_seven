import datetime

class Building:
    def __init__(self, name, description, cohorts):
        self.name = name
        self.description = description
        self.cohorts = cohorts
        self.date_created = datetime.datetime.now()
    
    def __str__(self) -> str:
        return self.name


class Cohort:
    def __init__(self, name, description, natives):
        self.name = name
        self.description = description
        self.natives = natives
        self.date_created = datetime.datetime.now()

    def __str__(self) -> str:
        return self.name


class Native:
    def __init__(self, scn, first_name, last_name, sex):
        self.scn = scn
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.date_created = datetime.datetime.now()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
