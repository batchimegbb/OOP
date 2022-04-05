#Create class Person
class Person:
    #Class attribute or properties
    organization =  "ASU"
    #Instance attributes (for each object)
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def age(self):
        #calculate the age from self.dob
        age= 0
        return age
    
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, Date of birth: {self.dob}"
    

#Create the Student (child class)
class Student(Person):
    def __init__(self, name, dob, grade, subjects):
        super().__init__(name, dob)
        self.grade = grade
        self.subjects = subjects

    def __repr__(self) -> str:
        return super().__repr__() + f", Grade: {self.grade}, Subjects: {self.subjects}"

#List of students
students =  []

#Main program
print("Welcome to ASU Student Services")
print("Please, enter students' information.")
print("---------------------------------")

while True:
    name = input("Name: ")
    dob = input("Date of Birth (yyyy/mm/dd): ")
    grade = input("Grade: ")
    subjects = input("Subjects: ")

    students.append(Student(name, dob, grade, subjects))

    answer = None
    while answer not in('yes', 'no'):
        anwer = (input("Would you like to enter another student (yes/no)? ")).lower()
    if answer=='no':
        #Print students
        print("You have entered the following students.") 
        print("---------------------------------")
        for student in students:
            print(student) 
        break
