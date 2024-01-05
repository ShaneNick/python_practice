from stack import Stack

# Introduction to the game
print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("left")
middle_stack = Stack("middle")
right_stack = Stack("right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = int(input("\nHow many disk do you want to play with?\n"))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

# Populate the left_stack with disks
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

# Calculate the optimal number of moves
num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

# Function to get user input for stack choice
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))
        user_input = input('')
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# Initialize the number of user moves
num_user_moves = 0

# Main game loop
while right_stack.get_size() != num_disks:
    # Print current state of stacks
    print("\n\n\n...Current Stacks....")
    for stack in stacks:
        stack.print_items()

    # Loop for each move
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()

        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        # Check if the move is valid and execute it
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1

            # Print stacks after the move
            print("\n\n...Stacks after the move....")
            for stack in stacks:
                stack.print_items()
            break
        else:
            print("\n\nInvalid Move. Try Again")

# Print completion message
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))
