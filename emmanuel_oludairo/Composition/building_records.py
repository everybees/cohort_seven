class Building:
    def __init__(self, building_name, address):
        self.building_name = building_name
        self.address = address
        self.cohorts = []

    def __str__(self):
        cohorts = ""
        for cohort in self.cohorts:
            cohorts += cohort + "\n"
        return self.building_name + "\n" + self.address + "\n" + cohorts


class Cohort:
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.cohort_natives = []

    def __str__(self):
        natives = ""
        for native in self.cohort_natives:
            natives += native + "\n"
        return self.cohort_name + "\n" + "SCN No. |   First Name  |   Last Name   |   Sex" + "\n" "==================================================" "\n" + natives


class Native:
    def __init__(self, sc_id, first_name, last_name, sex):
        self.sc_id = sc_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self):
        return self.sc_id + "\t\t|" + self.first_name + "\t\t\t|" + self.last_name + "\t\t\t|" + self.sex


def register_native_in_cohort(sc_id, first_name, last_name, sex):
    native = Native(sc_id, first_name, last_name, sex)
