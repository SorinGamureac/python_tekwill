notes = [10,8,5,7]
class Student:
    def __init__(self, *grade):
        self.grade = grade
        print(grade)
    
    @classmethod
    def average_of_grades(cls, grade):
        return cls(sum(grade)/len(grade))
mihai = Student(10)
mihai2 = Student.average_of_grades(notes)