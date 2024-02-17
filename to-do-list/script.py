import json

print('Please Choose One of the following options: Add, View, Delete')

answer = input()
request = answer.strip().lower()

# Read the existing data from the file, or initialize as empty if not found
def read_data():
    try:
        with open('to-do-list.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or empty file
        return {}

# Write updated data back to the file
def write_data(data):
    with open('to-do-list.json', 'w') as f:
        json.dump(data, f, indent=4)

if request == 'add':
    task = input("Enter your task: ")
    data = read_data()
    # Use an incremental numeric key; convert keys to integers for comparison
    task_key = max([int(k) for k in data.keys()], default=0) + 1
    data[str(task_key)] = task  # Ensure the key is stored as a string
    write_data(data)
    print("Task added.")
elif request == 'view':
    data = read_data()
    print(data)
elif request == 'delete':
    data = read_data()
    print(data)
    task_key = input("Which task number would you like to delete: ")
    # Ensure consistency in key data types; remove task if key exists
    if task_key in data:
        del data[task_key]
        write_data(data)
        print("Task deleted.")
    else:
        print("Task not found.")




