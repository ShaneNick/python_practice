# Importing the random module for selecting random elements
import random

# List containing possible weather conditions
weather = ["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"]

# List of days of the week
DOTW = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Prompting user to choose between today's forecast or this week's forecast
user_choice = input("Would you like 'today's forecast' or 'this week's forecast'? Enter 'today' or 'week': ")

# Display weather forecast based on user's choice
if user_choice.lower() == "today":
    # Randomly selecting a day and weather condition for today's forecast
    randomDOTW = random.randint(0, len(DOTW) - 1) 
    randomWeather = random.randint(0, len(weather) - 1)
    print("Today is " + DOTW[randomDOTW] + " and it will be " + weather[randomWeather])

elif user_choice.lower() == "week":
    # Displaying the week's forecast with a random weather condition for each day
    for day in DOTW:
        randomWeather = random.choice(weather)
        print("Today is " + day + " and it will be " + randomWeather)
