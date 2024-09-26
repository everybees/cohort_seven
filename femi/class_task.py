class Building(object):
    def __init__(self, name):
       self.name = name
       self.cohorts=[]

    def __str__(self) ->str:
        return self.name

    def add_cohorts_to_building(self, cohort):
        self.cohorts.append(cohort)
        


class Cohort(object):
    def __init__(self, name, description):
       self.name = name
       self.description = description
       self.natives=[]
       
    def __str__(self):
        return self.name
    
    def add_native_to_cohort(self, native):
        self.natives.append(native)

        
        

class Native(object):
    def __init__(self, first_name, last_name, sex, native_id):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.native_id=native_id

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name 


# def check_natives(native):
#     if native is not list:
#         raise ValueError
#     return nativep
