import json

# Function to load existing records from the JSON file
def load_records():
    try:
        with open('records.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        data = {"users": []}
    return data

# Function to save updated records to the JSON file
def save_records(records):
    with open('records.json', 'w') as file:
        json.dump(records, file)

# Main registration loop
while True:
    user_input = input("Enter a 6-10 digit number (or 'end' to quit): ")

    # Check if the user wants to end the program
    if user_input.lower() == 'end':
        break

    # Load existing records
    records = load_records()

    # Check if the number already exists
    # existing_users = user_input in records["users"] 
    if user_input in records["users"] :
        print("User already exists! L bozo")
    else:
        # Add new entry
        
        records["users"].append(user_input)
        save_records(records)
        print(f"Student #{user_input} has not participated yet 👍")

print("Program ended.")
