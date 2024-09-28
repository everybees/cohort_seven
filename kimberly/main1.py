import builtins
import class_task1
if __name__ == "__main__":
    global_container = []
    number_of_building = int(input("How many buildings do you want to generate: "))
    for i in range(number_of_building):
        name_of_building = input("Enter the name for building " + str(i+1) + ": ")
        description = input("Enter the address for " + name_of_building + ": ")
        building = Building(name_of_building, description)
        number_of_cohorts = int(input("Enter the number of cohorts in " + name_of_building + ": "))
        for i in range(number_of_cohorts):
            name_of_cohort = input("Enter name for cohort "+ str(i+1)+ ": " )
            cohort = Cohort(name_of_cohort)
            number_of_natives = int(input("Enter the number of natives in " + name_of_cohort + ": "))
            for i in range(number_of_natives):
                id_number = input("Enter id number for native " + str(i+1) + " in " + name_of_cohort +": ")
                first_name = input("Enter the firstname: ")
                last_name = input("Enter the lastname: ")
                gender = input("Enter gender type: ")
                native = Native(id_number, first_name, last_name, gender)
                cohort.cohort_natives.append(native.__str__())
            building.cohorts.append(cohort.__str__())
        global_container.append(building.__str__())

    for building in global_container:
        print(building)
# if __name__ == "__main__":
#     native1=[]
#     native_1=class_task1.Native("001","emma","jos","male")
#     native1.append(native_1)
#     native_2=class_task1.Native("002","giddy","udoh","male")
#     native1.append(native_2)
#     native_3=class_task1.Native("003","kim","oke","female")
#     native1.append(native_3)
#     native_4=class_task1.Native("004","tife","bolu","male")
#     native1.append(native_4)

#     native2=[]
#     native_1=class_task1.Native("005","segun","mac","male")
#     native2.append(native_1)
#     native_2=class_task1.Native("006","yetunde","ade","female")
#     native2.append(native_2)
#     native_3=class_task1.Native("007","isreal","fashina","male")
#     native2.append(native_3)
#     native_4=class_task1.Native("008","dami","omolori","female")
#     native2.append(native_4)

#     native3=[]
#     native_1=class_task1.Native("009","ozi","firebrand","female")
#     native3.append(native_1)
#     native_2=class_task1.Native("010","demola","ade","male")
#     native3.append(native_2)
#     native_3=class_task1.Native("011","tosin","aina","male")
#     native3.append(native_3)
#     native_4=class_task1.Native("012","precious","okoro","female")
#     native3.append(native_4)

#     native4=[]
#     native_1=class_task1.Native("013","solomon","tope","male")
#     native4.append(native_1)
#     native_2=class_task1.Native("014","ahmad","ola","male")
#     native4.append(native_2)
#     native_3=class_task1.Native("015","lantana","mohammed","female")
#     native4.append(native_3)
#     native_4=class_task1.Native("016","adesuwa","omo","female")
#     native4.append(native_4)

#     cohort=[]
#     cohort_1=class_task1.Cohort("cohort_one","jan,2020",native1)
#     cohort.append(cohort_1)
#     cohort_2=class_task1.Cohort("cohort_two","june,2020",native2)
#     cohort.append(cohort_2)
#     cohort_3=class_task1.Cohort("cohort_three","jan,2021",native3)
#     cohort.append(cohort_3)
#     cohort_4=class_task1.Cohort("cohort_four","june,2021",native4)
#     cohort.append(cohort_4)


#     building=class_task1.Building("Semicolon Village",cohort)
     
#     print("=" * 40)
#     print("Building Name: ",building.building_name)

#     for cohort in building.cohorts:
#         print("=" * 40)
#         print(cohort.cohort_name)
#         print(cohort.cohort_description)
#         print("=" * 40)
#         print("SCN No. | First Name | Last Name | Sex")
#         print("=" * 40)
#         for native in cohort.natives:
#             print(native.scn_no     +"    |   "         + native.first_name     +"  |   "       +    native.last_name       +"  |   "       +   native.sex)

