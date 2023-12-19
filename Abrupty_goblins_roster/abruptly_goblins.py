# List to store gamer information
gamers = []

def add_gamer(gamer, gamers_list):
    # Check if both 'name' and 'availability' keys exist in the gamer dictionary
    if "name" in gamer and "availability" in gamer:
        # Add gamer to the gamers list
        gamers_list.append(gamer)
    else:
        # Inform the user if the gamer dictionary is missing required keys
        print("Error: Gamer must contain a name and availability key")

gamer_2 = {"name": "kimberly", "availability": ["Mondays", "Tuesdays", "Fridays"]} 
add_gamer(gamer_2, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print(f"So far we have: {gamers}")
print("===================================")
def build_daily_frequency_table():
    days_of_the_week = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0
}
    return days_of_the_week


# Display current list of gamers
print("Current gamers list:")
for gamer in gamers:
    print(f"- {gamer['name']} available on {', '.join(gamer['availability'])}")
print("===================================")

def build_daily_frequency_table():
    # Create a dictionary for counting availability for each day of the week
    days_of_the_week = {
        "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0,
        "Friday": 0, "Saturday": 0, "Sunday": 0
    }
    return days_of_the_week

# Create a frequency table for availability
count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    # Calculate the availability of gamers for each day of the week
    for gamer in gamers_list:
        for day in gamer['availability']:
            if day in available_frequency:
                available_frequency[day] += 1

# Calculate availability based on the current gamers list
calculate_availability(gamers, count_availability)

# Display the calculated availability for each day
print("Availability count for each day:")
for day, count in count_availability.items():
    print(f"- {day}: {count}")
print("===================================")

def find_best_nights(availability_table):
    # Find the day with the highest availability
    best_night = max(availability_table, key=availability_table.get)
    return best_night

# Determine the best night for game night
game_night = find_best_nights(count_availability)
print(f"The best night for the game is: {game_night}")
print("===================================")

def available_on_night(gamers_list, day):
    # Create a list of gamers available on a specific day
    available = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            available.append(gamer['name'])
    return available

# Get the list of gamers available on the game night
attending_game_night = available_on_night(gamers, game_night)
print(f"Gamers available on {game_night}: {', '.join(attending_game_night)}")
print("===================================")

# Define the form_email string with placeholders
form_email = "Hello {name},\n\nYou are invited to play {game} on {day_of_week} night.\nHope to see you there!\n"

def send_email(gamers_who_can_attend, day, game):
    # Send an email to each gamer who can attend
    for gamer in gamers_who_can_attend:
        # Format the email string with each gamer's name and the specified day and game
        email = form_email.format(name=gamer, day_of_week=day, game=game)
        print(email)

# Send email invitations for the game night
send_email(attending_game_night, game_night, "Abruptly Goblins!")