from ozioma.building import class_task


def create_building(name, cohorts, address):
    building = class_task.Building(name, cohorts)
    return building


def create_cohort(name, natives, description):
    cohort = class_task.Cohorts(name,natives,description)
    return cohort


def create_native(first_name, last_name, native_id, gender):
    native = class_task.Native(first_name, last_name,native_id,gender)
    return native


def create_cohort_list():
    cohorts = []
    return cohorts


def create_native_list():
    natives = []
    return natives


def add_native_to_list(native):
    natives = create_native_list()
    return natives.append(native)


def add_cohort_to_list(cohort):
    cohorts = create_cohort_list()
    return cohorts.append(cohort)


def create_building_list():
    building = {}
    return building


def add_cohort_to_building(cohort):
    building = create_building_list()
    return building[cohort]