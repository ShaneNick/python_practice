# Importing classes for the linked list and the flower definitions
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

# Define the HashMap class
class HashMap:
    # Constructor for the HashMap class
    def __init__(self, size):
        # Initialize the size of the array
        self.array_size = size
        # Create an array of LinkedLists for separate chaining
        self.array = [LinkedList() for i in range(self.array_size)]

    # Hash function to convert a key into a hash code
    def hash(self, key):
        # Convert key to bytes and sum their ASCII values to create a hash code
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    # Compressor function to convert hash code into an array index
    def compressor(self, hash_code):
        # Use modulo operation to ensure index is within array bounds
        return hash_code % self.array_size

    # Function to assign a key-value pair in the hash map
    def assign(self, key, value):
        # Get the index for this key using the hash and compressor functions
        array_index = self.compressor(self.hash(key))
        # Access the linked list at the calculated index
        list_at_array = self.array[array_index]

        # Iterate through the linked list
        for item in list_at_array:
            # If the key is found, update its value
            if item[0] == key:
                item[1] = value
                return
        # If the key is not found, insert a new node with the key-value pair
        list_at_array.insert(Node([key, value]))

    # Function to retrieve a value by its key in the hash map
    def retrieve(self, key):
        # Get the index for this key
        array_index = self.compressor(self.hash(key))
        # Access the linked list at the index
        list_at_index = self.array[array_index]

        # Iterate through the linked list
        if list_at_index is not None:
            for item in list_at_index:
                # If the key is found, return its value
                if item[0] == key:
                    return item[1]
        # Return None if the key is not found
        return None

# Create a new instance of HashMap
blossom = HashMap(len(flower_definitions))
# Populate the hash map with flower definitions
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('begonia'))
