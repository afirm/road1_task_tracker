"""
The list of commands and their usage is given below:

# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
Task Properties
Each task should have the following properties:

id: A unique identifier for the task
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
"""
#user=input("Name?")
#print("Welcome, {}. What do you want to do? (help for list of commands.)".format(user))
import json, os
from datetime import datetime
print(os.path.exists("tasks.json"))

def add(s):
    cur_time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("tasks.json", "r") as file:
            tasks=json.load(file)
        curr_task_id=tasks[-1]["id"]+1
    except:
        tasks=[]
        curr_task_id=1
    current_task={"id":curr_task_id,"description":s,"status":"todo", "createdAt":cur_time,"updatedAt":cur_time}

    tasks.append(current_task)

    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=4)
    print("Task added successfully! (ID={})".format(curr_task_id))
    main()

def update(s):
    print(s)
def delete(id):
    if id=="all":
        with open("tasks.json","w") as file:
            #print(new_tasks)
            json.dump([], file, indent=4)
        print("All tasks deleted.")
        return main()
    else:
        try:
            id=int(id)
        except:
            print("unknown id")
            return main()

    with open("tasks.json","r") as tasks:
        tasks=json.load(tasks)
        new_tasks=[]
        i=0
        for dic in tasks:
            if dic["id"]!=id:
                new_tasks.append(dic)
                #print(f"task {dic["id"]} is not it")
                i+=1
        if i == len(tasks):
            print("no task with id {} found.".format(id))
            return main()

    with open("tasks.json","w") as file:
        #print(new_tasks)
        json.dump(new_tasks, file, indent=4)
    print("task (id={}) deleted".format(id))
    main()
    
def mark_in_progress(s):
    print(s)
def mark_done(s):
    print(s)

def list(j=True):
    try:
        with open("tasks.json","r") as file:
            tasks=json.load(file)
            for task in tasks:
                print(f">>> [ {task['id']} ] - [ {task['description']} ]'s status is [ {task['status']} ]")
            if tasks == []:
                print("task list is empty.")
    except:
        print("No task found.")
    return main()

def main():
    com=input("What to do?")
    if com[:3]=="add":
        task_name=com[4:]
        add(task_name)
    if com[:4]=="list":
        try:
            list(com[5:])
        except:
            list()
    if com[:len("delete")]=="delete":
        #print(com[len("delete")+1:])
        delete(com[len("delete")+1:])


main()