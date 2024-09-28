"""

create a class of building
create a class of cohorts
create a class of natives

create an object of a building that has 4 cohorts and these cohorts have natives.

print the builiding name, the cohorts with their name and description, not forgetting the natives in these
cohorts with their first name, last name, and their native id(SCN1 and so on).

we can have something like this:

Building Name: Semicolon Village

Cohort One Natives:
SCN No. | First Name | Last Name | Sex
--------------------------------------
SCN01   | John       | Doe       | Male
....


"""
class Building:
    def __init__(self, building_name, cohorts):
        self.building_name = building_name
        self.cohorts=cohorts
    
    def __str__(self) -> str:
        return self.building_name

class Cohort:
    def __init__(self, cohort_name,cohort_description,natives):
        self.cohort_name=cohort_name
        self.cohort_description=cohort_description
        self.natives=natives

        
    def __str__(self) -> str:
        return self.cohort_name 
        
        

    # def create_cohort_in_building(cohort_name,cohort_description):
    #     cohort_in_building=Cohort(cohort_name,cohort_description)
    #     return cohort_in_building
        
    
class Native:
    def __init__(self, scn_no, first_name, last_name, sex):
        self.scn_no=scn_no
        self.first_name = first_name
        self.last_name = last_name
        self.sex =sex
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
        
    # def create_native_in_cohort(scn_no,first_name,last_name,sex):
    #     native_in_cohort=Native(scn_no,first_name,last_name,sex)
    #     return native_in_cohort
            


