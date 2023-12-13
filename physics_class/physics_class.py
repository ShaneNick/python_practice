# Initial setup for the "Use the Force" exercise
train_mass = 22680            # Mass of the train in kilograms
train_acceleration = 10       # Acceleration of the train in meters per second squared
train_distance = 100          # Distance over which the train is traveling in meters
bomb_mass = 1                 # Mass of a bomb in kilograms

# Function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9  # Conversion formula
    return c_temp

# Convert 100 degrees Fahrenheit to Celsius
f100_in_celsius = f_to_c(100)

# Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = (c_temp * 9/5) + 32  # Conversion formula
    return f_temp

# Convert 0 degrees Celsius to Fahrenheit
c0_in_fahrenheit = c_to_f(0)

# Function to calculate force
def get_force(mass, acceleration):
    return mass * acceleration  # Force formula (Newton's second law)

# Calculate the force of the train
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function to calculate energy
def get_energy(mass, c=3*10**8):
    return mass * c**2  # Energy formula from E=mc^2

# Calculate the energy of a 1kg bomb
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

# Function to calculate work done
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)  # Calculate force
    work = force * distance                # Work formula (Work = Force x Distance)
    return work

# Calculate the work done by the train
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
