class Building:
    def __init__(self, building_name):
        self.building_name=building_name
        
    
    def __str__(self):
        return self.building_name + " " + self.cohorts


class Cohort:
    def __init__(self, cohort_name, cohort_description):
        self.cohort_name = cohort_name
        self.cohort_description = cohort_description
        
    def __str__(self):
        return self.cohort_name + " " + self.cohort_description + " " + self.natives


class Native:
    def __init__(self, first_name, last_name, sex, age, cohort_id):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.cohort_id = cohort_id

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.sex + " " + self.age + " " + self.cohort_id

        
