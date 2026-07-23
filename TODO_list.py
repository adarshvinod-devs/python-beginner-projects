from datetime import datetime , date
import json

try:
    with open("TODO.json","r") as file:
        task_list = json.load(file)

except FileNotFoundError:
    task_list = {}

def add_task():
    task_name = input("Enter task title: ")
    task_discription = input("Enter task discription: ")
    date_str = input("Enter due date(DD-MM-YYYY): ")
    created_date = date.today().strftime("%d-%m-%Y")
    task_list[task_name] = {"Discription":task_discription,"Due Date":date_str,"Task added on":str(created_date)}
    with open("TODO.json","w") as file:
        json.dump(task_list,file)

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
    name = input("Enter task title to remove: ")
    if name in task_list:
        del task_list[name]
        with open ("TODO.json","w") as file:
            json.dump(task_list,file)
    else:
        print("Couldn't find the task with that title")

view_task()
