from class_task import *


global natives, cohort_details


def register_natives(first_name, last_name, gender, sc_id):
    global natives

    natives = ""
    native = Native(first_name, last_name, gender, sc_id).__str__()

    natives += native + "\n"


def add_native():
    number_of_natives = 1
    while number_of_natives < 2:
        register_natives(first_name=input("Enter first name: "), last_name=input("Enter last "
                                                                                 "name: "),
                         gender=input("Enter gender: "), sc_id=("sc" + input("Enter cohort: ") +
                                                                str(number_of_natives)))
        print("\n")
        number_of_natives += 1

    return natives


def add_cohort():
    global natives, cohort_details
    number_of_cohort = 1

    while number_of_cohort < 3:
        cohort_details = Cohort(cohort_number=input("Enter cohort number"), cohort_name=input("Enter cohort name"))
        # cohort_natives = add_native()
        Building.cohort["Cohort {0}".format(str(number_of_cohort))] = add_native()
        print("\n\n")
        number_of_cohort += 1

    return cohort_details, Building.cohort


def add_building():
    building = Building("Semicolon Africa")
    add_cohort()
    for key, value in building.cohort.items():
        print(cohort_details.__str__)
        print(key + "\n" + value)


add_building()
