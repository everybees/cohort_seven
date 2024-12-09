class Building:
    def __init__(self, building_name, description, cohorts):
        self.building_name = building_name
        self.cohorts = []
        self.description = description

    def __str__(self) -> str:
        cohorts = ""
        for cohort in self.cohorts:
            cohorts += cohort + "\n"
        return self.building_name + "\n" + self.description + "\n\n" + cohorts
    #
    #
    # @property
    # def building_name(self):
    #     return self.building_name
    #
    # @property
    # def description(self):
    #     return self.description
    #
    # @property
    # def cohorts(self):
    #     return self.cohorts
    #
    # @building_name.setter
    # def building_name(self, building_name):
    #     if len(building_name) > 100:
    #         raise ValueError("Name cannot exceed 30 characters")
    #     self.building_name = building_name
    #
    # @descrription.setter
    # def description(self, description):
    #     if len(description) > 100:
    #         raise ValueError("Name cannot exceed 30 characters")
    #     self.description = description



class Cohort:
    def __init__(self, cohort_names, cohort_description):
        self.cohorts_names = cohort_names

        self.cohorts_natives = []

    def __str__(self) -> str:
        natives = ""
        for native in self.cohorts_natives:
            natives+= native +"\n"
        return "NAME OF COHORT: "+self.cohorts_names + "\n\n " + "Scn No.| First Name   | Last Name   | Sex" + "\n"+"-----------------------------------------------------"+"\n"+ natives


class Native:
    def __init__(self, scn_no, first_name, last_name, sex):
        self.scn_no = scn_no
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self) -> str:
        return self.scn_no +"\t|" +self.first_name + "\t\t " + self.last_name +"\t\t|" + self.sex

