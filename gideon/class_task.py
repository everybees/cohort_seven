class Building:
    def __init__(self, building_name, cohorts):
        self.building_name = self._building_name(building_name)
        self.cohorts = cohorts
    def __str__(self) -> str:
        return self.building_name


    def _building_name(self, building_name):
        if len(building_name) > 35:
            raise ValueError("Name cannot exceed 35 characters")
        return building_name
    # def _cohorts(self, cohorts):
    #     if type is not list:
    #         raise ValueError("Cohorts must be a list")
    #     return cohorts


class Cohort:
    def __init__(self, cohort_name, cohort_description, native):
        self.cohort_name = self._cohort_name(cohort_name)
        self.cohort_description = cohort_description
        self.native = native
    def __str__(self) -> str:
        return self.cohort_name + " " + self.cohort_description


    def _cohort_name(self, cohort_name):
        if len(cohort_name) > 30:
            raise ValueError("Cohort Name cannot exceed 20 characters")
        return cohort_name
    # def _cohort_description(self, cohort_description):
    #     if type is not str:
    #         raise ValueError("Cohort Description must be a String")
    #     return cohort_description
    # def _native(self, native):
    #     if type is not list:
    #         raise ValueError("Native must be a list")
    #     return native

class Natives:
    def __init__(self, first_name, last_name, sex, id):
        self.first_name = self._first_name_(first_name)
        self.last_name = self._last_name_(last_name)
        self.sex = sex
        self.id = id
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.sex + " " + self.id

    def _first_name_(self, first_name):
        if len(first_name) > 20:
            raise ValueError("First Name must not be more than 20 characters")
        return first_name
    def _last_name_(self, last_name):
        if len(last_name) > 20:
            raise ValueError("First Name must not be more than 20 characters")
        return last_name
    # def _id_(self, id):
    #     if type is not int:
    #         raise ValueError("id has to be of type int")
    #     return id

    def _sex(self, sex):
        sex = sex.lower()
        if sex != "male" and sex != "male":
            raise ValueError("Sex must be either male or female")
        return sex