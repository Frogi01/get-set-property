class College:
    def __init__(self, name, num_students, campus):
        self._name = name
        self._num_students = num_students
        self._campus = campus

    
    def get_name(self):
        return self._name

    
    def set_name(self, name):
        self._name = name


    def get_num_students(self):
        return self._num_students

    
    def set_num_students(self, num_students):
        self._num_students = num_students

    
    def get_campus(self):
        return self._campus

    
    def set_campus(self, campus):
        self._campus = campus
        
college = College("VPK", 2000, "Vernadskogo")
print(college._name) 
print(college._num_students)
print(college._campus)

college.name = "Энергоколледж"
college.num_students = 1600
college.campus = "Кировский"
print(college.name) 
print(college.num_students) 
print(college.campus) 