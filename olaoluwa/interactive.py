class Building:
    def __init__(self, building_name, address):
        self.Building = building_name
        self.address = address
        self.cohorts = []

    def __str__(self):
        cohorts = ""
        for cohort in self.cohorts:
            cohorts += cohort + "\n"
        return self.Building + "\n" + self.address + "\n" + cohorts


class Cohort:
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.cohort_native = []

    def __str__(self):
        natives = ""
        for native in self.cohort_native:
            natives += native + "\n"
        return self.cohort_name + "\n" + "SCN No.   |   First Name  |   Last Name   |   Sex" + "\n" + natives


class Native:
    def __init__(self, sc_id, first_name, last_name, sex):
        self.sc_id = sc_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self):
        return self.sc_id + "\t|" + self.first_name + "\t\t|" + self.last_name + "\t\t|" + self.sex


def register_native_in_cohort(sc_id, first_name, last_name, sex):
    native = Native(sc_id, first_name, last_name, sex)
