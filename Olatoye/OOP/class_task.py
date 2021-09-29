class Native:
    def __init__(self, first_name, last_name, gender, sc_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.sc_id = sc_id

    def __str__(self):
        return str(self.sc_id) + "\t\t|" + self.first_name + "\t\t|" + self.last_name + "\t\t|" + self.gender


class Cohort:
    natives = []

    def __init__(self, cohort_number, cohort_name):
        self.cohort_number = cohort_number
        self.cohort_name = cohort_name

    def __str__(self):
        return self.cohort_number + "\t" + self.cohort_name


class Building:
    cohort = {}

    def __init__(self, building_name, building_address):
        self.building_name = building_name
        self.building_address = building_address

    def __str__(self):
        return self.building_name + "\n" + self.building_address
