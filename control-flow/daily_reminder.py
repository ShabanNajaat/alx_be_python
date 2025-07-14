# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        print("Invalid priority level. Defaulting to low priority.")
        priority_message = "low priority task"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."

# Provide a customized reminder
print(reminder)
