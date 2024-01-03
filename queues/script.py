from node import Node

class Queue:
    def __init__(self, max_size=None):
        # Initialize the queue with optional max_size and set initial size to 0
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def enqueue(self, value):
        # Add an item to the queue if there's space
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            
            # If the queue is empty, set both head and tail to the new item
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                # Otherwise, add the new item to the end of the queue
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
         
    def dequeue(self):
        # Remove and return the item at the front of the queue if not empty
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            
            # If there's only one item, set both head and tail to None
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                # Otherwise, set the head to the next item in the queue
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")
  
    def peek(self):
        # Return the value of the front item in the queue if not empty
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")
  
    def get_size(self):
        # Return the current size of the queue
        return self.size
  
    def has_space(self):
        # Check if the queue has space to add more items
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.get_size()
    
    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0

# Example use of the Queue class
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)

print("Adding orders to our deli line...\n------------")
# Adding multiple orders to the deli queue
orders = [
    "egg and cheese on a roll",
    "bacon, egg, and cheese on a roll",
    "toasted sesame bagel with butter and jelly",
    # ... [other orders] ...
]
for order in orders:
    deli_line.enqueue(order)

print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")

# Dequeue and serve all orders
while not deli_line.is_empty():
    deli_line.dequeue()
