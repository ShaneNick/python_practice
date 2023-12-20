class Circle:
    # Class variable representing the approximation of pi
    pi = 3.14

    def __init__(self, diameter):
        # Constructor that initializes a Circle instance with a given diameter
        print("Creating circle with diameter {d}".format(d=diameter))
        # Set the radius of the circle as half the diameter
        self.radius = diameter / 2
  
    def circumference(self):
        # Method to calculate the circumference of the circle
        return self.pi * 2 * self.radius

# Creating an instance of Circle representing a medium pizza
medium_pizza = Circle(12)
# Creating an instance of Circle representing a teaching table
teaching_table = Circle(36)
# Creating an instance of Circle representing a round room
round_room = Circle(11460)

# Print the circumference of the medium pizza circle
print("Circumference of medium pizza: {:.2f}".format(medium_pizza.circumference()))
# Print the circumference of the teaching table circle
print("Circumference of teaching table: {:.2f}".format(teaching_table.circumference()))
# Print the circumference of the round room circle
print("Circumference of round room: {:.2f}".format(round_room.circumference()))
