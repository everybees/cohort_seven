class Building:
    def __init__(self, name, cohorts):
        self.name = name
        self.cohorts = cohorts

    def __str__(self) -> str:
        return self.name


class Cohort:
    def __init__(self, name, description, natives):
        self.name = name
        self.description = description
        self.natives = natives

    def __str__(self) -> str:
        return self.name

class Native:
    def __init__(self, first_name, last_name, sex, native_id):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.native_id = native_id

        def _native_first_name(first_name):
            if len(first_name) > 25:
                raise ValueError("First name cannot exceed 25 characters, you know what to abi?")
            return first_name

    def _native_last_name(last_name):
        if len(last_name) > 25:
            raise ValueError("last name cannot exceed 25 characters")
        return last_name

    def _native_sex(sex):
        if sex != "male" and sex != "female":
            raise ValueError("sex must either be male or female")
        return sex

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
