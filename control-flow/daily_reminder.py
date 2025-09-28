task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task_description}' is a high priority task.  Consider completing it when you have free time")
        else:
            print("Please specify a valid time-bound input (yes/no)")
    case "medium":
        if time_bound == "yes":
            print(f"Notice: '{task_description}' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Notice: '{task_description}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Please specify a valid time-bound input (yes/no)")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task_description}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task_description}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Please specify a valid time-bound input (yes/no)")
    case _:
        print("Please specify a valid task priority (high/medium/low)")
