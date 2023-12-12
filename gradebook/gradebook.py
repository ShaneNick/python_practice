# List of grades from the last semester
last_semester_gradebook = [
    ["politics", 80],
    ["latin", 96],
    ["dance", 97],
    ["architecture", 65]
]

# Subjects for this semester
subjects = ["Physics", "Calculus", "Poetry", "History"]

# Grades for this semester
grades = [98, 97, 85, 88]

# Create a new gradebook for this semester
gradebook = [
    ["Physics", 98],
    ["Calculus", 97],
    ["Poetry", 85],
    ["History", 89]
]

# Print current gradebook
print(gradebook)

# Add "Computer Science" subject with grade 100
gradebook.append(["Computer Science", 100])

# Print updated gradebook
print(gradebook)

# Add "Visual Arts" subject with grade 93
gradebook.append(["Visual Arts", 93])

# Modify the grade for "Visual Arts" by adding 5 points
gradebook[5][1] = 93 + 5

# Print updated gradebook
print(gradebook)

# Remove the numerical grade from "Poetry"
gradebook[2].remove(85)

# Print updated gradebook
print(gradebook)

