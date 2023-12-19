import csv
import json

# List to store compromised user names
compromised_users = []

# Read from passwords.csv and collect usernames
with open("passwords.csv", 'r') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])
    print("Usernames extracted from passwords.csv.")

# Write the usernames to compromised_users.txt
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + '\n')
    print("Usernames written to compromised_users.txt.")

# Create a JSON message for the boss
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {
        "recipient": "The Boss",
        "message": "Mission Success"
    }
    json.dump(boss_message_dict, boss_message)
    print("Message for the boss written to boss_message.json.")

# Slash Null's signature
slash_null_sig = r"""
_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

# Write Slash Null's signature to new_passwords.csv
with open('new_passwords.csv', 'w') as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)
    print("Slash Null's signature written to new_passwords.csv.")
