from precious.oop.object_oriented_programming.object_oriented_programming import *


if __name__ == "__main__":

    global_container = []
    building = []
    cohort_detail = []

    def buildings():
        number_of_building = int(input("Enter number of buildings: \n--->"))
        for i in range(number_of_building):
            building_name = ("Semicolon Village")
            address = ("312 Herbert Macaulay, Sabo, Yaba")
            building_ = Building(building_name, address)
            global_container.append(building_.__str__())


    buildings()

    def add_cohort():

        number_of_cohorts = int(input("Enter Number Of Cohort You want in a building:\t"))
        cohort_name = input("Enter Cohort Name:\t")
        cohort_number = input("Enter Cohort Number:\t")
        for i in range(number_of_cohorts):
            cohort = Cohort(cohort_name, cohort_number)
            building.cohort_detail.append(cohort.__str__())


    add_cohort()

    def add_natives():
        number_of_natives = int(input("Enter Number Of Natives You want in a Cohort:\n" + "--->"))
        for i in range(number_of_natives):
            sc_id = input("Enter your Semi colon id no:\n" + "--->")
            first_name = input("Enter First Name:\n" + "--->")
            last_name = input("Enter Last name:\n" + "--->")
            sex = input("Enter Sex:\n" + "--->")
            native = Native(sc_id, first_name, last_name, sex)
            cohort.cohort_natives.append(native.__str__())

    add_natives()
    for building in global_container:
        print(building)



# cohort_1.cohort_natives.append(native_1.__str__())
# main_building.cohorts.append


# add_cohort()


# for key in Building.cohorts.keys():
#     print(key)
#     for value in Building.cohorts.values():
#         print(value, end="")
# def news() -> Type[Building]:
#     return Building
#

# print(Building.__str__(Building(building_name="Semicolon Village", address="312 Herbert Macaulay, Sabo, Yaba")))
# for key in Building.cohorts.keys():
#     print(key)
#     for value in Building.cohorts.values():
#         print(value, end="")
# print(main_building)

# run = building()
# for key in run.keys():
#     print(key)
#     for value in run.values():
#         for key in Building.cohorts.keys():
#             print(key)
#             for value in Building.cohorts.values():
#                 print(value)

