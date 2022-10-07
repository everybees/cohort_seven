
 Building:
     def __init__(self, name, description, cohorts):
        self.name = name
        self.description = description
        self.cohort = cohorts
        self.date_created = date
     def __str__(self) -> str:
        return self.name