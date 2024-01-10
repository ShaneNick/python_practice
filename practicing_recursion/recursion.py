# Define build_bst() below...
def build_bst(my_list):
    # Base case: If list is empty
    if not my_list:
        return "No Child"

    # Finding the middle index and value
    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]

    # Printing the middle index and value
    print("Middle index: " + str(middle_idx))
    print("Middle value: " + str(middle_value))

    # Creating the current tree node
    tree_node = {"data": middle_value}

    # Recursive calls for the left and right subtrees
    # Left half: everything before the middle index
    tree_node["left_child"] = build_bst(my_list[:middle_idx])
    # Right half: everything after the middle index
    tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])

    return tree_node

sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
