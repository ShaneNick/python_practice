question1 = "What are the four Grand Slam tournaments in tennis?"
answer1 = "Wimbledon, French Open, US Open, Australian Open"

question2 = "How many points are needed to win a standard game in tennis?"
answer2 = "4"

question3 = "What is a 'love' score in tennis?"
answer3 = "0"

question4 = "What surface is Wimbledon played on?"
answer4 = "grass"

question5 = "Can you name a basic tennis stroke used both in offense and defense?"
answer5 = ["forehand", "backhand"]

count = 0
#validation logic

# Ask the first question and check the answer
user_answer1 = input(question1 + "\nYour answer: ")
if user_answer1.lower() == answer1.lower():
    print("Correct")
    count += 1
else:
    print("Wrong")

# Ask the second question and check the answer
user_answer2 = input(question2 + "\nYour answer: ")
if user_answer2.lower() == answer2:
    print("Correct")
    count += 1
else:
    print("Wrong")


# Ask the third question and check the answer
user_answer3 = input(question3 + "\nYour answer: ")
if user_answer3.lower() == answer3:
    print("Correct")
    count += 1
else:
    print("Wrong")

# Ask the fourth question and check the answer
user_answer4 = input(question4 + "\nYour answer: ")
if user_answer4.lower() == answer4:
    print("Correct")
    count += 1
else:
    print("Wrong")

# Ask the fifth question and check the answer
user_answer5 = input(question5 + "\nYour answer: ").lower()
if user_answer5 in answer5:
    print("Correct")
    count += 1
else:
    print("Wrong")


print("You scored a total of: " + str(count) + "/5")