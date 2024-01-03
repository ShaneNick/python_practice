# Importing the Node class from node module
from node import Node

class Stack:
    def __init__(self, limit=1000):
        # Initialize the stack with a top item, size, and a limit
        self.top_item = None
        self.size = 0
        self.limit = limit
  
    def push(self, value):
        # Push a new item onto the stack if there's space
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            # Print a message if the stack is full
            print("No room for {}!".format(value))

    def pop(self):
        # Remove the top item from the stack if it's not empty
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        # Print a message if the stack is empty
        print("All out of pizza.")

    def peek(self):
        # Return the value of the top item if the stack is not empty
        if not self.is_empty():
            return self.top_item.get_value()
        # Print a message if the stack is empty
        print("Nothing to see here!")

    def has_space(self):
        # Check if the stack still has space
        return self.limit > self.size

    def is_empty(self):
        # Check if the stack is empty
        return self.size == 0
  
# Creating an instance of Stack with a limit of 6 items
pizza_stack = Stack(6)

# Adding pizzas to the stack
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Trying to add a seventh pizza, which should fail due to stack limit
pizza_stack.push("pizza #7")

# Displaying the first pizza to be delivered and then delivering pizzas
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Trying to pop from an empty stack, which should show a message
pizza_stack.pop()
