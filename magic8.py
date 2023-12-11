# Import the random module to use its functions
import random

# Store the user's name
name = input("Please input your name")

# Store the user's question
question = input("Please ask a question")

# Initialize the answer variable with an empty string
answer = ""

# Generate a random number between 1 and 9 (inclusive)
random_number = random.randint(1, 9)

# Commented out line: used for debugging to see the generated random number
#print(random_number)

# Determine the answer based on the random number
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer= "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else: 
  answer = "Error"  # Fallback answer in case of an unexpected random_number

# Print the user's question and the magic 8 ball's answer
if not name:
    print(" asks: " + str(question) + "?")
    print("Magic 8 ball's answer: " + str(answer))
elif not question:
    print("Please enter a question")
else:
    print(str(name) + " asks: " + str(question) + "?")
    print("Magic 8 ball's answer: " + str(answer))





