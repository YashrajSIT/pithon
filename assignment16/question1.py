class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # Getter methods
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    # Setter methods
    def set_name(self, name):
        self._name = name
    
    def set_age(self, age):
        self._age = age

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self._student_id = student_id
        self._major = major
    
    # Getter methods
    def get_student_id(self):
        return self._student_id
    
    def get_major(self):
        return self._major
    
    # Setter methods
    def set_student_id(self, student_id):
        self._student_id = student_id
    
    def set_major(self, major):
        self._major = major

class Professor(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self._employee_id = employee_id
        self._department = department
    
    # Getter methods
    def get_employee_id(self):
        return self._employee_id
    
    def get_department(self):
        return self._department
    
    # Setter methods
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
    
    def set_department(self, department):
        self._department = department

class School:
    def __init__(self):
        self.students = []
        self.professors = []
    
    # Method to add a new student
    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Invalid student object.")
    
    # Method to add a new professor
    def add_professor(self, professor):
        if isinstance(professor, Professor):
            self.professors.append(professor)
        else:
            print("Invalid professor object.")
    
    # Method to display all students
    def display_all_students(self):
        print("List of Students:")
        for student in self.students:
            print(f"Name: {student.get_name()}, Age: {student.get_age()}, Student ID: {student.get_student_id()}, Major: {student.get_major()}")
    
    # Method to display all professors
    def display_all_professors(self):
        print("List of Professors:")
        for professor in self.professors:
            print(f"Name: {professor.get_name()}, Age: {professor.get_age()}, Employee ID: {professor.get_employee_id()}, Department: {professor.get_department()}")

# Example usage:
if __name__ == "__main__":
    # Creating instances of Student and Professor
    student1 = Student("Alice", 20, "S001", "Computer Science")
    student2 = Student("Bob", 21, "S002", "Mathematics")
    
    professor1 = Professor("Dr. Smith", 45, "P001", "Physics")
    professor2 = Professor("Dr. Johnson", 50, "P002", "Computer Science")
    
    # Creating a School object
    school = School()
    
    # Adding students and professors to the school
    school.add_student(student1)
    school.add_student(student2)
    
    school.add_professor(professor1)
    school.add_professor(professor2)
    
    # Displaying all students and professors
    school.display_all_students()
    print("\n")
    school.display_all_professors()