class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        # Node initialization with a value and optional next and previous nodes
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    def set_next_node(self, next_node):
        # Set the next node pointer of this node
        self.next_node = next_node
    
    def get_next_node(self):
        # Return the next node this node points to
        return self.next_node

    def set_prev_node(self, prev_node):
        # Set the previous node pointer of this node
        self.prev_node = prev_node
    
    def get_prev_node(self):
        # Return the previous node this node points to
        return self.prev_node
  
    def get_value(self):
        # Return the value stored in this node
        return self.value
    

class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list
        self.head_node = None
        self.tail_node = None
  
    def add_to_head(self, new_value):
        # Add a new node with the given value to the beginning of the list
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            # If list is not empty, update current head's previous node
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node is None:
            # If the list was empty, new node is also the tail
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        # Add a new node with the given value to the end of the list
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            # If list is not empty, update current tail's next node
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            # If the list was empty, new node is also the head
            self.head_node = new_tail

    def remove_head(self):
        # Remove the head node from the list
        removed_head = self.head_node

        if removed_head is None:
            # If the list is empty, return None
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node is not None:
            # If the list still has nodes, set new head's previous node to None
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            # If the removed head was the only node, call remove_tail()
            self.remove_tail()

        return removed_head.get_value()
