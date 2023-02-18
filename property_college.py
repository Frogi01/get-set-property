class College:
    def __init__(self, name, num_students, campus):
        self._name = name
        self._num_students = num_students
        self._campus = campus

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def num_students(self):
        return self._num_students

    @num_students.setter
    def num_students(self, num_students):
        self._num_students = num_students

    @property
    def campus(self):
        return self._campus

    @campus.setter
    def campus(self, campus):
        self._campus = campus
        
college = College("VPK", 2000, "Vernadskogo")
print(college.name) 
print(college.num_students)
print(college.campus)

college.name = "Энергоколледж"
college.num_students = 1600
college.campus = "Кировский"
print(college.name) 
print(college.num_students) 
print(college.campus) 