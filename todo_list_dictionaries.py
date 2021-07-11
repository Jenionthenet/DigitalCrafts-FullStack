tasks = []

def view_task_list(lines):
    i = 1
    for task in tasks:
        print(f"{i} - {task['title']} - {task['priority']}")
        i += 1

while True:

    print ("")
    print("1 to Add Tasks")
    print("2 to Delete Tasks")
    print("3 to View All Tasks")
    print("q to Quit ")
    print("")

    option = (input("Enter your option: "))

    if option == "q":
            break

    elif option == "1":
        title = input("Enter your task: ")
        priority = input("Enter the task priority level 'high', 'medium', or 'low': ")
        task_dict = {"title" : title, "priority" : priority}
        tasks.append(task_dict)
        #print(task_dict)

    elif option == "2":
        view_task_list(tasks)
        print("")
        deleted_task = int(input("Enter the task number that you wish to delete: "))
        del tasks[deleted_task -1]

    elif option == "3":
        view_task_list(tasks)
        
    
    else:
        print("Please enter a choice from the menu.")






