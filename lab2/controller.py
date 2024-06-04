from model.model import Storage

class Controller:
    def __init__(self, storage: Storage):
        self.storage = storage
        
    def add_student(self, name: str, course: int, group: int, total_works: int, completed_works: int, programming_language: str):
        return self.storage.add_student(name, course, group, total_works, completed_works, programming_language)

    def get_all_students(self):
        return self.storage.students
    
    def get_students_by_group(self, group_number):
        return self.storage.get_students_by_group(group_number)
    
    def get_students_by_name(self, name):
        return self.storage.get_students_by_name(name)

    def get_students_by_course(self, course):
        return self.storage.get_students_by_course(course)

    def get_students_by_programming_language(self, language):
        return self.storage.get_students_by_programming_language(language)

    def get_students_by_completed_works(self, completed_works):
        return self.storage.get_students_by_completed_works(completed_works)

    def get_students_by_total_works(self, total_works):
        return self.storage.get_students_by_total_works(total_works)

    def get_students_by_uncompleted_works(self, uncompleted_works):
        return self.storage.get_students_by_uncompleted_works(uncompleted_works)
    

    def delete_students_by_group(self, group_number):
        return self.storage.delete_students_by_group(group_number)

    def delete_students_by_name(self, name):
        return self.storage.delete_students_by_name(name)

    def delete_students_by_course(self, course):
        return self.storage.delete_students_by_course(course)

    def delete_students_by_programming_language(self, language):
       return self.storage.delete_students_by_programming_language(language)

    def delete_students_by_completed_works(self, completed_works):
        return self.storage.delete_students_by_completed_works(completed_works)

    def delete_students_by_total_works(self, total_works):
        return self.storage.delete_students_by_total_works(total_works)

    def delete_students_by_uncompleted_works(self, uncompleted_works):
        return self.storage.delete_students_by_uncompleted_works(uncompleted_works)
