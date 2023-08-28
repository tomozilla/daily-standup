def generate_daily_tasks(day, today_tasks, yesterday_tasks=None):
    output = f"{day}\n"
    
    if yesterday_tasks:
        output += "Yesterday :\n" + "\n".join([f"* {task}" for task in yesterday_tasks]) + "\n"
    
    output += "Today :\n" + "\n".join([f"* {task}" for task in today_tasks])
    return output

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    common_tasks = ["Calendar review", "Viviun review"]
    
    daily_tasks = {}
    
    for day in days:
        print(f"Enter tasks for {day} (type 'done' when finished):")
        tasks_for_day = []
        
        while True:
            task = input("> ")
            if task.lower() == 'done':
                break
            tasks_for_day.append(task)
        
        daily_tasks[day] = tasks_for_day + common_tasks
        print("---")
    
    for i, day in enumerate(days):
        if i == 0:
            print(generate_daily_tasks(day, daily_tasks[day]))
        else:
            print(generate_daily_tasks(day, daily_tasks[day], daily_tasks[days[i-1]]))
        print("---")

if __name__ == "__main__":
    main()
