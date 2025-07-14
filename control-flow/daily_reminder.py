# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        priority_level = "high"
    case "medium":
        priority_level = "medium"
    case "low":
        priority_level = "low"
    case _:
        print("Invalid priority level. Defaulting to low priority.")
        priority_level = "low"

# Provide a customized reminder
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_level} priority task that requires immediate attention today!")
else:
    print(f"Reminder: '{task}' is a {priority_level} priority task. Consider completing it when you have free time.")

