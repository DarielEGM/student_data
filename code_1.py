class Student:
    def __init__(self, Name, Age, School_Grade):
        self.Name = Name
        self.Age = Age
        self.School_Grade = School_Grade
    
    def informationStudent(self):
        print(f"The student's name is {self.Name}, age is {self.Age}, and grade is {self.School_Grade}.")
        
Name = input("What is your name?: ")   
Age = input("How are you?: ")   
School_Grade = input("What is your School Grade?: ")   

student1 = Student(Name, Age, School_Grade)

student1.informationStudent()