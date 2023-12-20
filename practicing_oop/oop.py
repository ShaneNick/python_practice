class Student:
    def __init__(self, name, year):
        self.name = name  # Assigning the name parameter to the name attribute
        self.year = year  # Assigning the year parameter to the year attribute
        self.grades = []  # Initializing an empty list for grades

    def add_grade(self, grade):
        # Adding a grade to the grades list if it's an instance of Grade
        if isinstance(grade, Grade):
            self.grades.append(grade)
            print(f"Added grade with score {grade.score} to {self.name}")

class Grade:
  #Class-level attribute set to 65
    minimum_passing = 65
  #Initializes score to represent the grades numerical value
    def __init__(self, score):
        self.score = score
    #This method is checking to see if the min is 65
    def is_passing(self):
        passing = self.score >= self.minimum_passing
        print(f"Grade score {self.score} is {'passing' if passing else 'not passing'}")
        return passing



        

    def __init__(self, score):
        self.score = score  # Assigning the score parameter to the score attribute

# Creating student instances
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Creating a new Grade instance with a score of 100
grade = Grade(100)
print(f"Created grade with score: {grade.score}")
# Adding the created grade to pieter's grades
pieter.add_grade(grade)
