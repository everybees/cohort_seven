import class_task

if __name__ == "__main__":
    natives1 = []
    natives2 = []
    natives3 = []
    natives4 = []

    cohorts = []
    native1 = class_task.Native("John", "Eba", "M", "SCN01")
    natives1.append(native1)

    native2 = class_task.Native("Good", "News", "M", "SCN02")
    natives1.append(native2)

    native3 = class_task.Native("Kim", "Killer", "F", "SCN03")
    native4 = class_task.Native("Leo", "Morris", "M", "SCN04")
    native5 = class_task.Native("Mac", "Manuel", "F", "SCN05")
    native6 = class_task.Native("Jamie", "Lanister", "F", "SCN06")
    native7 = class_task.Native("Sam", "Joe", "M", "SCN09")
    native8 = class_task.Native("Aimie", "Lan", "F", "SCN07")
    natives2.append(native3)
    natives2.append(native4)
    natives2.append(native5)
    natives3.append(native6)
    natives3.append(native7)
    natives4.append(native8)

    new_cohort = class_task.Cohort("cohort_one", "first cohort admitted into semicolon", natives1)
    cohorts.append(new_cohort)
    new_cohort = class_task.Cohort("cohort_two", "second cohort accepted into semicolon", natives2)
    cohorts.append(new_cohort)
    new_cohort = class_task.Cohort("cohort_three", "third cohort accepted into semicolon", natives3)
    cohorts.append(new_cohort)
    new_cohort = class_task.Cohort("cohort_four", "fourth cohort accepted into semicolon", natives4)
    cohorts.append(new_cohort)
    building = class_task.Building("Semicolon Village", cohorts)
    print(building.name)

    for cohort in building.cohorts:
        if cohort.name == "cohort_one":
            print(cohort.name + ":")
            print("SCN  No.|   First name   |   Last name   |   Sex")
            for native in cohort.natives:
                print(
                    native.native_id + "        |"+ native.first_name + "          |"+ native.last_name + "         |"+ native.sex)

            print(
                "\n=====================================================================================================")

        elif cohort.name == "cohort_two":
            print(cohort.name + ":")
            print("SCN  No.|   First name   |   Last name   |   Sex")
            for native in cohort.natives:
                print(
                    native.native_id + "        |" + native.first_name + "          |" + native.last_name + "         |" + native.sex)

            print(
                "\n=====================================================================================================")

        elif cohort.name == "cohort_three":
            print(cohort.name + ":")
            print("SCN  No.|   First name   |   Last name   |   Sex")
            for native in cohort.natives:
                print(
                    native.native_id + "        |" + native.first_name + "          |" + native.last_name + "         |" + native.sex)
            print(
                "\n=====================================================================================================")
        else:
            print(cohort.name + ":")
            print("SCN  No.|   First name   |   Last name   |   Sex")
            for native in cohort.natives:
                print(
                    native.native_id + "        |" + native.first_name + "          |" + native.last_name + "         |" + native.sex)
            print(
                "\n=====================================================================================================")
