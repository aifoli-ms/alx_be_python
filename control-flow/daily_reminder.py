# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop to keep checking until valid priority is given
valid_priorities = ["high", "medium", "low"]
while priority not in valid_priorities:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Generate reminder using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Schedule it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be addressed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to fit it into your day.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but still needs to be done today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")