class Building:
    # cohorts = {}

    def __init__(self, building_name, address):
        self.building_name = building_name
        self.address = address
        self.cohorts = []

    def __str__(self):
        cohorts = ""
        for cohort in self.cohorts:
            cohorts += cohort + "\n"
        return self.building_name + "\n" + self.address + "\n\n", cohorts


class Cohort:
    cohort_natives = []

    def __init__(self, cohort_name, cohort_number):
        self.cohort_name = self._cohort_name_(cohort_name)
        self.cohort_number = self._cohort_number_(cohort_number)
        # self.cohort_natives = []

    def _cohort_name_(self, cohort_name):
        if len(cohort_name) > 15:
            raise ValueError("cohort name can not exceed 15 characters")
        return cohort_name

    def _cohort_number_(self, cohort_number):
        if len(cohort_number) <= 0:
            raise ValueError("cohort number can not be lesser than 1: ")
        return cohort_number

    def __str__(self):
        natives = ""
        for native in self.cohort_natives:
            natives += native + "\n"
            # print(native + "\n")
        return (self.cohort_name + self.cohort_number + "\n\n" + "SCN No. | First Name    | Last Name     | Sex" + "\n" + \
               "----------------------------------------------" + " \n"), self.cohort_natives


class Native:
    def __init__(self, sc_id, first_name, last_name, sex):
        self.sc_id = sc_id
        self.first_name = self._native_first_name(first_name)
        self.last_name = self._native_last_name(last_name)
        self.sex = self._native_sex(sex)

    def _native_first_name(self, first_name):
        if len(first_name) > 25:
            raise ValueError("first name can not exceed 25 characters")
        return first_name

    def _native_last_name(self, last_name):
        if len(last_name) > 25:
            raise ValueError("Last Name cannot exceed 25 characters")
        return last_name

    def _native_sex(self, sex):
        sex = sex.lower()
        if sex != "male" and sex != "female":
            raise ValueError("Sex must be either male or female")
        return sex

    def __str__(self) -> str:
        return self.sc_id + "\t\t|" + self.first_name + "\t\t|" + self.last_name + "\t\t|" + self.sex
