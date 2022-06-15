# This code will add info about the student.
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

# This code below will show if a student is on honor roll or not.
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False