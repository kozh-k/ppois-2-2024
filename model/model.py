class Storage:
    def __init__(self):
        self.students = []
        
    def add_student(self, name: str, course: int, group: int, total_works: int, completed_works: int, programming_language: str):
        self.students.append(Student(name, course, group, total_works, completed_works, programming_language))


    def get_students_by_group(self, group_number):
        found_students = []
        for student in self.students:
            if student.group == group_number:
                found_students.append(student)
        return found_students
    
    def get_students_by_name(self, name):
        found_students = []
        for student in self.students:
            if student.name == name:
                found_students.append(student)
        return found_students

    def get_students_by_course(self, course):
        found_students = []
        for student in self.students:
            if student.course == course:
                found_students.append(student)
        return found_students

    def get_students_by_programming_language(self, language):
        found_students = []
        for student in self.students:
            if student.programming_language == language:
                found_students.append(student)
        return found_students

    def get_students_by_completed_works(self, completed_works):
        found_students = []
        for student in self.students:
            if student.completed_works == completed_works:
                found_students.append(student)
        return found_students

    def get_students_by_total_works(self, total_works):
        found_students = []
        for student in self.students:
            if student.total_works == total_works:
                found_students.append(student)
        return found_students

    def get_students_by_uncompleted_works(self, uncompleted_works):
        found_students = []
        for student in self.students:
            total_works = int(student.total_works)
            completed_works = int(student.completed_works)
            if total_works - completed_works == uncompleted_works:
                found_students.append(student)
        return found_students


    def delete_students_by_group(self, group_number):
        self.students = [student for student in self.students if student.group != group_number]

    def delete_students_by_name(self, name):
        self.students = [student for student in self.students if student.name != name]

    def delete_students_by_course(self, course):
        self.students = [student for student in self.students if student.course != course]

    def delete_students_by_programming_language(self, language):
        self.students = [student for student in self.students if student.programming_language != language]

    def delete_students_by_total_works(self, total_works):
        self.students = [student for student in self.students if student.total_works != total_works]

    def delete_students_by_completed_works(self, completed_works):
        self.students = [student for student in self.students if student.completed_works != completed_works]

    def delete_students_by_uncompleted_works(self, uncompleted_works):
        self.students = [student for student in self.students if (student.total_works - student.completed_works) != uncompleted_works]
        
class Student:
    def __init__(self, name: str, course: int, group: int, total_works: int, completed_works: int, programming_language: str):
        self.name = name
        self.course = course
        self.group = group
        self.total_works = total_works
        self.completed_works = completed_works
        self.programming_language = programming_language
        
    def __str__(self):
        return f"       {self.name}       |      {self.course}       |         {self.group}        |        {self.total_works}        |         {self.completed_works}             |       {self.programming_language}"
