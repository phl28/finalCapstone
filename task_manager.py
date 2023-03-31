# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

def reg_user(username_password):
    '''Add a new user to the user.txt file'''
    while True:
        # - Request input of a new username
        new_username = input("New Username: ")

        # check if username already exists
        if new_username in username_password:
            print("This username already exists")
            continue
        break

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

    return username_password

def add_task(username_password, task_list):
    '''Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
    - A username of the person whom the task is assigned to,
    - A title of a task,
    - A description of the task and 
    - the due date of the task.'''

    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return 
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
    return 

def view_all(task_list):
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
    return 

def view_mine(task_list):
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    # initialise k to keep track of the task number
    k = 1
    # initialise a dict to keep track of which task that number refers to
    task_dict = {}
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task {k}: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            task_dict[k] = t['title']
            print(disp_str)
            k += 1

    # allow user to select either a specific task by entering a number or input '-1' to return to the main menu 
    decision = int(input("Select either a specific task(by entering the task number) or input -1 to return to the main menu: "))

    # returning to main menu if -1
    if decision == -1:
        return task_list
    
    # if decision is between 0 and k ,this means that the user has identified a task to edit
    elif 0 < decision < k:
        # loop through the task_list and see which task that the user wants to edit
        for t in task_list:
            # check if the task if the one we are looking for
            if t['username'] == curr_user and task_dict[decision] == t['title']:
                # make sure the user is entering a valid decision
                while True:
                    # allows user to decide what has to be done, either mark a task as complete or edit the task
                    decision2 = input("Select either to mark the task as complete or edit the task by inputting 1 or 2 respectively (-1 to exit): ")
                    if decision2 == "1":
                        t['completed'] = True
                        break
                    elif decision2 != "2" and t['completed'] == False:
                        new_username = input("Enter the username of the person whom the task will be assigned to (press enter if nothing needs to be changed): ")
                        if new_username != "":
                            t['username'] = new_username
                        while True:
                            try:
                                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                                t['due_date'] = due_date_time
                                break

                            except ValueError:
                                print("Invalid datetime format. Please use the format specified")
                        break
                    elif decision2 == "-1":
                        break
        
        # overwrite the tasks into the tasks.txt file
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))

        return task_list

def gen_reports(task_list, username_password):
    completed_task = 0
    incomplete_overdue = 0
    curr_date = date.today()
    ''' for each entry in users_tasks, the key is the username and the values is a list with the first value being the number of tasks assigned,
     the second value being the number of tasks completed and third value is the number of tasks overdue and not completed'''
    users_tasks = {}
    for t in task_list:

        if t['username'] not in users_tasks:
            users_tasks[t['username']] = [1, 0, 0]
        else:
            users_tasks[t['username']][0] += 1

        if t['completed'] == True:
            completed_task += 1
            if len(users_tasks[t['username']]) == 1:
                users_tasks[t['username']][1] = 1
            else:
                users_tasks[t['username']][1] += 1
        elif t['completed'] == False and t['due_date'].date() < curr_date:
            incomplete_overdue += 1
            if len(users_tasks[t['username']]) == 2:
                users_tasks[t['username']][2] = 1
            else:
                users_tasks[t['username']][2] += 1
            

    num_tasks = len(task_list)
    uncompleted = num_tasks - completed_task

    # generate the reports as required with the information all laid out clearly also to make our lives easier later when we want to output for th admin
    with open("task_overview.txt", "w") as task_file:
        task_file.write(f"Total number of tasks that have been generated and tracked: {num_tasks}\n")
        task_file.write(f"Total number of completed tasks: {completed_task}\n")
        task_file.write(f"Total number of uncompleted tasks: {uncompleted}\n")
        task_file.write(f"Total number of tasks that haven't been completed and that are overdue: {incomplete_overdue}\n")
        task_file.write(f"Percentage of tasks that are incomplete: {(uncompleted / num_tasks) * 100}%\n")
        task_file.write(f"Percentage of tasks that are overdue: {(incomplete_overdue / num_tasks) * 100}%\n")


    # number of users
    num_users = len(username_password)

    # similar to the task report 
    with open("user_overview.txt", "w") as user_file:
        user_file.write(f"Total number of users registered: {num_users}\n")
        user_file.write(f"Total number of tasks that have been generated and tracked: {num_tasks}\n")
        for username in users_tasks.keys():
            user_file.write(f"Username: {username}\n")
            user_file.write(f"Total numner of tasks assigned: {users_tasks[username][0]}\n")
            user_file.write(f"Percentage of the total number of tasks that have been assigned: {users_tasks[username][0] / num_tasks * 100}%\n")
            user_file.write(f"Percentage of the tasks assgned that have been completed: {users_tasks[username][1] / users_tasks[username][0] * 100}%\n")
            user_file.write(f"Percentage of the tasks assigned that must still be completed: {(users_tasks[username][0] - users_tasks[username][1]) / users_tasks[username][0] * 100}%\n")
            user_file.write(f"Percentage of the tasks assigned that have not yet been completed and are overdue: {users_tasks[username][2]/ users_tasks[username][0] * 100}%\n")

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    # call the reg_user function if the user types 'r'
    if menu == 'r':
        username_password = reg_user(username_password)

     # call the add_task function if the user types 'a'
    elif menu == 'a':
        add_task(username_password, task_list)

     # call the view_all function if the user types 'va'
    elif menu == 'va':
        view_all(task_list)

     # call the view_mine function if the user types 'vm'    
    elif menu == 'vm':
        task_list = view_mine(task_list)

     # call the gen_reports function if the user types 'gr'         
    elif menu == "gr":
        gen_reports(task_list, username_password)

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

        # check if the files are already present
        try:
            task_f = open('task_overview.txt', 'r')
            user_f = open('user_overview.txt', 'r')
            task_lines = task_f.readlines()
            user_lines = user_f.readlines()
            task_f.close()
            user_f.close()

            for line in task_lines:
                print(line)

            print("-----------------------------------")  
            for line in user_lines:
                print(line)

        # ask admin to generate the reports first 
        except FileNotFoundError:
            print("text files don't exist, please first generate them through the generate reports option")
            



    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")