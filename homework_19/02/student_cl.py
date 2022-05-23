class Student:
    def __init__(self, name, group, grades):
        self.full_name = name
        self.group = group
        self.grades = grades
        self.average_grade = sum(grades) / len(grades)
