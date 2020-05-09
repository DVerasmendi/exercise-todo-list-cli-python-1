import csv
todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    todos.append(title)
    return todos
    pass

def print_list():
    contador=1
    global todos
    for x in todos:
        print(str(contador)+': '+x)
        contador=contador+1
    pass

def delete_task(number_to_delete):
    # your code here
    number_to_delete=int(number_to_delete)
    number_to_delete=number_to_delete-1
    todos.pop(number_to_delete)
    return todos
    pass

def save_todos():
    file_tareas=""
    i=0
    for x in todos:
        if i==0:
            #print(x['name'])
            file_tareas=file_tareas +x
            i=i+1
        else:
            file_tareas=file_tareas+','+x
    print(file_tareas)

    file_to_save=open("list_tareas.csv","w+")
    file_to_save.write(file_tareas)
    file_to_save.close()
    pass

    
def load_todos():
    # your code here
    file=open("list_tareas.csv","r")
    csv_file=csv.reader(file)
    for row in csv_file:
        #print(row)
        lista=row
        for x in lista:
            #print(x)
            if x not in todos:
                todos.append(x)
    #print(todos)
    file.close()   
    return todos
    pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
            
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")