class Student:
   def __init__(self, name, course, group, total_works, completed_works, programming_language):
      self.name = name
      self.course = course
      self.group = group
      self.total_works = total_works
      self.completed_works = completed_works
      self.programming_language = programming_language

class Storage:
    def __init__(self):
        self.students = []
        
    def add_student(self, id: int, fio: str, group_number: int):
        self.students.append(Student(id, fio, group_number))