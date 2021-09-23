class Native:
    def __init__(self, first_name, last_name, gender, sc_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.sc_id = sc_id

    def __str__(self):
        return str(self.sc_id) + " " + self.first_name + " " + self.last_name + " " + self.gender


class Cohort:
    def __init__(self, cohort_number, cohort_name):
        self.cohort_number = cohort_number
        self.cohort_name = cohort_name
        self.natives = []

    def __str__(self):
        for native in self.natives:
            return self.cohort_number + " " + self.cohort_name + "\n" + native


class Building:
    def __init__(self, building_name):
        self.building_name = building_name
        self.cohorts = {}

    def __str__(self):
        for key, value in self.cohorts:
            return self.building_name + "\n" + key + "\n" + value
