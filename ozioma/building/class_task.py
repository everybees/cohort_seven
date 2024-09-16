
class Building:
    def __init__(self, name, cohorts):
        self.name = self._check_building_name(name)
        self.cohorts = self._check_cohorts(cohorts)

    def __str__(self):
        return self.name + "," + self.cohorts

    def _check_building_name(self, building_name):
        if len(building_name) > 20:
            raise ValueError("Building name is too long.")
        if type(building_name) is not str:
            raise ValueError("Input is not applicable here.")
        return building_name

    def _check_cohorts(self, cohort):
        if type(cohort) is not list:
            raise ValueError("Invalid cohort type.")
        return cohort


class Cohorts:
    def __init__(self, cohort_name, natives, description):
        self.cohort_name = self._check_cohort_name(cohort_name)
        self.cohort_description = description
        self.natives = self._check_native(natives)

    def __str__(self):
        return self.cohort_name

    def _check_cohort_name(self, cohort_name):
        if type(cohort_name) is not str:
            raise ValueError("Invalid cohort name!")
        if len(cohort_name) > 25:
            raise ValueError("Cohort name too long")
        return cohort_name

    def _check_native(self, native_id):
        if native_id is not list:
            raise ValueError("Invalid native input.")
        return native_id


class Native:
    def __init__(self, first_name, last_name, _native_id, gender):
        self.first_name = self._check_first_name(first_name)
        self.last_name = self._check_last_name(last_name)
        self.native_id = _native_id
        self.gender = self._check_gender(gender)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def _check_first_name(self, first_name):
        if type(first_name) != str:
            raise ValueError("Invalid first name!")
        if len(first_name) > 24:
            raise ValueError("Name is longer than 24 characters.")
        return first_name

    def _check_last_name(self, last_name):
        if type(last_name) != str:
            raise ValueError("Invalid first name!")
        if len(last_name) > 24:
            raise ValueError("Name is longer than 24 characters.")
        return last_name

    def _check_gender(self, gender):
        new_gender = gender.lower()
        if new_gender is not "male" and new_gender is not "female":
            raise ValueError("Invalid input.")
        return new_gender

    def _check_native_id(self, native_id):
        if native_id is not int:
            raise ValueError("Invalid input")
        return native_id