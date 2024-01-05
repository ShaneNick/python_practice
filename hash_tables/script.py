class HashMap:
    def __init__(self, array_size):
        # Constructor: Initializes the hash map with a specified array size.
        # Each slot of the array is initially set to None.
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        # Hash function: Converts a key into a hash code.
        # count_collisions is used to modify the hash for collision handling.
        key_bytes = key.encode()  # Converts the key into bytes.
        hash_code = sum(key_bytes)  # Sums the bytes to create a hash code.
        return hash_code + count_collisions  # Adjusts hash based on collisions.

    def compressor(self, hash_code):
        # Compressor function: Reduces a hash code to a valid array index.
        return hash_code % self.array_size

    def assign(self, key, value):
        # Assigns a key-value pair to the hash map.
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # If the spot is empty or the key already exists, assign the value.
        if current_array_value is None or current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Handle collisions.
        number_collisions = 1
        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None or current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

    def retrieve(self, key):
        # Retrieves a value by key from the hash map.
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        # If the slot is empty or the key matches, return the value.
        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        # Handle retrieval in case of collisions.
        retrieval_collisions = 1
        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

# Example usage of the HashMap
hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

# Retrieving values
print(hash_map.retrieve('gabbro'))  # Output: igneous
print(hash_map.retrieve('sandstone'))  # Output: sedimentary
print(hash_map.retrieve('gneiss'))  # Output: metamorphic
