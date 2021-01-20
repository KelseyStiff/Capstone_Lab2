
#importing dataclass
from dataclasses import dataclass

@dataclass
class Student:
    #initialization of class attributes
    name: str
    school_id: str
    gpa: float

    #__str__ method returns formatted string of Student attributes
    def __str__(self):
        return f'Name {self.name}, ID: {self.school_id} GPA: {self.gpa}'


def main():
    #testing class by creating alex student object
    alex = Student('Alex', 'audfh', 2.7)
    #printing just student objects name
    print(alex.name)

    #printing formatted version of student object
    print(alex)
    
    #creating second student object
    sam = Student('Sam', 'haiude', 3.6)
    print(sam)

#calling main method
main()