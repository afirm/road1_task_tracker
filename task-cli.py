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
    id = s.split(" ")[0]
    desc=" ".join(s.split(" ")[1:])
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks=json.load(file)
            newtasks=[]
            changed =False
            try:
                for task in tasks:
                    if task['id']== int(id):
                        task["description"] = desc
                        newtasks.append(task)
                        changed = True
                        msg = f"Task {id} updated successfully."
                    else:
                        newtasks.append(task)
                        if not changed:
                            msg =f"No task with id {id} found."

                with open("tasks.json","w") as file:
                    json.dump(newtasks,file,indent=4)
                    print(msg)
            except:
                print(f"{id} is not a valid id.")
                return main()
    else:
        print(f"no task found")
        return main()
    main()

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
    
def mark_in_progress(s=False):
    with open("tasks.json","r") as file:
        tasks=json.load(file)
        newtasks=[]
        changed=False
        try:
            for task in tasks:
                if task["id"]==int(s):
                    task["status"] = "in progress"
                    changed=True
                    newtasks.append(task)
                else:
                    newtasks.append(task)
        except:
            s= "Please give an id" if s == "" else f"'{s}' is not a valid id."
            return main(s)

        if changed:
            with open("tasks.json", "w") as file:
                json.dump(newtasks, file, indent=4)
            return main(f"Task {s} was successfully marked as in progress")
        else:
            return main(f"No tasks with id {s} found")
            
    

def mark_done(s=False):
    with open("tasks.json","r") as file:
        tasks=json.load(file)
        newtasks=[]
        changed=False
        try:
            for task in tasks:
                if task["id"]==int(s):
                    task["status"] = "done"
                    changed=True
                    newtasks.append(task)
                else:
                    newtasks.append(task)
        except:
            s= "Please give an id" if s == "" else f"'{s}' is not a valid id."
            return main(s)

        if changed:
            with open("tasks.json", "w") as file:
                json.dump(newtasks, file, indent=4)
            return main(f"Task {s} was successfully marked as done")
        else:
            return main(f"No tasks with id {s} found")
            
def mark_todo(s=False):
    with open("tasks.json","r") as file:
        tasks=json.load(file)
        newtasks=[]
        changed=False
        try:
            for task in tasks:
                if task["id"]==int(s):
                    task["status"] = "todo"
                    changed=True
                    newtasks.append(task)
                else:
                    newtasks.append(task)
        except:
            s= "Please give an id" if s == "" else f"'{s}' is not a valid id."
            return main(s)

        if changed:
            with open("tasks.json", "w") as file:
                json.dump(newtasks, file, indent=4)
            return main(f"Task {s} was successfully marked as todo")
        else:
            return main(f"No tasks with id {s} found")
    

def list(j=True):
    if j=="todo" or j=="done" or j =="in progress":
        try:
            jtasks = 0
            with open("tasks.json","r") as file:
                tasks=json.load(file)
                for task in tasks:
                    if task['status']== j:
                        print(f">>> [ {task['id']} ] - [ {task['description']} ]'s status is [ {task['status']} ]")
                        jtasks=+1
                if jtasks == 0:
                    print(f"no task is marked {j}.")
                else:
                    print(f"{jtasks} out of {len(tasks)} tasks marked as {j}.")
                return main()
        except:
            print("No task found.")
    else:
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

def main(msg=False):
    if msg:
        print(msg)
    com=input("What to do?")
    if com[:3]=="add":
        task_name=com[4:]
        add(task_name)
    elif com[:4]=="list":
        try:
            list(com[5:])
        except:
            list()
    elif com[:len("delete")]=="delete":
        #print(com[len("delete")+1:])
        delete(com[len("delete")+1:])
    elif com[:len("update")]=="update":
        update(com[len("update")+1:])

    elif com[:len("mark_in_progress")] in ("mark_in_progress", "mark-in-progress", "mark in progress", "mark in-progress","mark in_progress",):
            mark_in_progress(com[len("mark_in_progress")+1:])

    elif com[:len("mark_done")] in ("mark_done", "mark-done", "mark done",):
            mark_done(com[len("mark_done")+1:])

    elif com[:len("mark_todo")] in ("mark_todo", "mark-todo", "mark todo",):
            mark_todo(com[len("mark_todo")+1:])
    else:
        print('''not a proper command. Use:
              add [task name]
              update [task ID] [new task name]
              delete [task delete]
              list [empty for all tasks, "todo", "in-progress", and "done" for tasks with that status]
              mark done [task ID]
              mark in-progress [task ID]
              mark todo [task ID]
              ''')
        main()
main()