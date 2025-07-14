# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task with match-case
match priority:
    case "high":
        if time_bound == "yes":
            message = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            message = f"'{task}' is a high priority task."
    case "medium":
        if time_bound == "yes":
            message = f"'{task}' is a medium priority task that requires immediate attention today!"
        else:
            message = f"'{task}' is a medium priority task."
    case "low":
        if time_bound == "yes":
            message = f"'{task}' is a low priority task that requires immediate attention today!"
        else:
            message = f"'{task}' is a low priority task."
    case _:
        message = "Invalid priority level entered. Please try again with high, medium, or low."

# Print the standardized reminder format
if priority in ["high", "medium", "low"] and time_bound in ["yes", "no"]:
    if time_bound == "yes":
        print(f"\nReminder: {message}")
    else:
        print(f"\nNote: {message}")
else:
    print(message)

# Success message (keep this exactly as specified)
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")