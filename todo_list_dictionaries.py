tasks = []

while True:

    print("1 to Add Tasks")
    print("2 to Delete Tasks")
    print("3 to View All Tasks")
    print("q to Quit ")

    option = (input("Enter your option number: "))



    if option == "1":
        title = input("Enter your task: ")
        priority = input("Enter the task priority level 'high', 'medium', or 'low': ")
        task_dict = {"title" : title, "priority" : priority}
        tasks.append(task_dict)
        print(task_dict)

    elif option == "2":
        i = 1
        for task in tasks:
            print(f"{i} - {task['title']} - {task['priority']}")
            i += 1
        deleted_task = int(input("Enter the task number that you wish to delete: "))
        del tasks[deleted_task -1]

    elif option == "3":
        i = 1
        for task in tasks:
            print(f"{i} - {task['title']} - {task['priority']}")
            i += 1
        
    
    elif option == "q":
        break






