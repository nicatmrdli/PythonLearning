class Student:
# "class" is an overview of what the student data type is.
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
# "self" is referring to an actual object.