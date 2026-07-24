from datetime import datetime , date
import json

try:
    with open("TODO.json","r") as file:
        task_list = json.load(file)

except FileNotFoundError:
    task_list = {}

def add_task():
    while True:
     task_name = input("Enter task title: ")
     if task_name in task_list:
        print("Task title already exists. Try a different Title. ")
     else:
        task_discription = input("Enter task discription: ")
        date_str = input("Enter due date(DD-MM-YYYY): ")
        created_date = date.today().strftime("%d-%m-%Y")
        task_list[task_name] = {"Discription":task_discription,"Due Date":date_str,"Task added on":str(created_date)}
        with open("TODO.json","w") as file:
            json.dump(task_list,file)
        break
  

def view_task():
    sorted_task_list = sort_task()
    for  key,value in sorted_task_list:
        print(f"• {key}")
        print("============================")
        for nested_key,nested_value in value.items():
            print(f"{nested_key} : {nested_value}\n")

def sort_task():
    sorted_task_list = sorted(task_list.items(), key= lambda item: datetime.strptime(item[1]["Due Date"],"%d-%m-%Y").date())
    return sorted_task_list

def remove_task():
    while True:
        name = input("Enter task title to remove(Enter 'q' to exit): \n")
        if name == 'q' or name == 'Q':
            break
        elif name in task_list:
            del task_list[name]
            with open ("TODO.json","w") as file:
                json.dump(task_list,file)
            break
        else:
            print("Couldn't find the task with that title")
            reprompt = (input("Press 'r' to retry\n"))
            if reprompt != 'r' and reprompt != 'R':
                break

def edit_task():
    while True:
        name = input("Enter the task title to edit: \n")
        fields = ["1 -> Task title","2 -> Task discription","3 -> Due Date","4 ->Exit"]
        if name in task_list:
            while True:
                for i in fields: print(i)
                try:
                    field = int(input("Enter which field to edit:\n"))
                    match field:
                        case 1:
                            task_title = input("Enter new task title:\n")
                            task_list[task_title] = task_list.pop(name)
                            name = task_title
                        case 2:
                            task_discription = input("Enter new task discription:\n")
                            task_list[name]["Discription"] = task_discription
                        case 3:
                            due_date = input("Enter new due date(DD-MM-YYYY) :\n")
                            task_list[name]["Due Date"] = due_date
                        case 4:
                            return
                        case _:
                            print("Invalid choice")
                    with open("TODO.json","w") as file:
                        json.dump(task_list,file)

                except ValueError:
                    print("Invalid Input")
        else :
            reprompt = input("Could not find a task with that title. Enter 'r' to retry: \n")
            if reprompt.lower() != 'r':
                break




def menu():    
    options = ["1 -> Add Task","2 -> View Tasks","3 -> Edit Task","4 -> Remove Task","5 -> Exit"]
    while True:
        for i in options:
            print(i)
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    add_task()
                case 2:
                    view_task()
                case 3:
                    edit_task()
                case 4:
                    remove_task()
                case 5:
                    break
                case _ :
                    print("Enter a valid choice")
        except ValueError:
            print("Invalid input")

menu()


