'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date
from tkinter import E
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
contents = ""
user_username_list = []
user_password_list = []
task_count_list = []
user_count_list=[]

validate_name = 1
validate_password = 1

with open('user.txt', 'r+') as f:
        for line in f:
              user_input = line
              user_username = user_input.split(", ")  
              if (user_input=="\n"):
                  print ("")
              else: 
                  user_username_list.append(user_username[0])
                  user_password_list.append(user_username[1])
                  
control_var = 1
control_var1 = 1

username = str(input("Please enter your username :  "))
password = str(input("Please enter your password :  "))
check = 0 

while(control_var==1):
    for i in range(0, len(user_username_list)):
          if(username==user_username_list[i]):
               check = i     
               validate_name=0
    if(validate_name==1):
        username = str(input("Username entered is invalid! Please enter a valid username :  "))
    if(validate_name==0):
        control_var =0

while(control_var1==1):
    if(password==user_password_list[check].strip()):
               validate_password=0
    if(validate_password==1):
        password = str(input("Password entered is invalid! Please enter a valid password :  "))
    if(validate_password==0):
        control_var1 =0
               
print("Successful login!")

control_password = 1
while True:
      if(username=="admin"):
          choice = str(input('''Select one of the following Options below: 
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
sv - view user statistics
e - Exit '''))
      else:
          choice = str(input('''Select one of the following Options below: 
a - Adding a task
va - View all tasks
vm - view my task
e - Exit '''))
      
      choice = choice.lower()
      menu = choice
      
      if menu == 'r':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

        if(username=="admin"):
            new_username = str(input("Please enter a new username : "))
            new_password = str(input("Please enter a new password : "))
            confirm_password = str(input("Please confirm new password : "))
            if(new_password==confirm_password):
                control_password=0

            while(control_password==1):
                confirm_password = str(input("Passwords do not match. Please confirm new password : "))
                if(new_password==confirm_password):
                    control_password=0
        
            user_username_list.append(new_username)
            user_password_list.append(new_password)

            with open('user.txt','w') as f:  
                for j in range(0, len(user_username_list)):
                    f.write(f"{user_username_list[j]}, {user_password_list[j]}") 
                
        else:
            print("You do not have access to this")

      elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        today = date.today()
        
        username_task_assign = str(input("Please enter the username of who the task is assigned to :  "))
        username_task_assign = username_task_assign.strip()
        title_task = str(input("Please enter the Title of the task  :  "))
        title_task = title_task.strip()
        description_task = str(input("Please enter the description of the task :  "))
        description_task = description_task.strip()
        current_date = today.strftime("%d %b %Y")
        due_date_task = str(input("Please enter the due date of the task : [Day Month Year] "))
        due_date_task = due_date_task.strip()
    
        task_list = []

        with open('tasks.txt', 'r+') as f:
            for line in f:
               task_input = line
               task_list.append(task_input)
        
        new_task_input = (f"\n{username_task_assign}, {title_task}, {description_task}, {current_date}, {due_date_task}, No")
        task_list.append(new_task_input)
        
        with open('tasks.txt','w') as f:  
            for k in range(0, len(task_list)):
                f.write(f"{task_list[k]}") 

      elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        with open('tasks.txt', 'r+') as f:
            for line in f:
               task_view = line
               individual_task_view = line.split(", ")
               #print(individual_task_view[0])
               print(f"Task                   {individual_task_view[1]} ")
               print(f"Assigned to:           {individual_task_view[0]} ")
               print(f"Date assigned:         {individual_task_view[3]} ")
               print(f"Due date:              {individual_task_view[4]} ")
               print(f"Date assigned:         {individual_task_view[5].strip()} ")
               print(f"Task Description:      {individual_task_view[2]} ")

      elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
 
        with open('tasks.txt', 'r+') as f:
            for line in f:
                task_view = line
                individual_task_view = line.split(", ")
               #print(individual_task_view[0])
                if(individual_task_view[0]==username):    
                    print(f"Task                   {individual_task_view[1]} ")
                    print(f"Assigned to:           {individual_task_view[0]} ")
                    print(f"Date assigned:         {individual_task_view[3]} ")
                    print(f"Due date:              {individual_task_view[4]} ")
                    print(f"Date assigned:         {individual_task_view[5].strip()} ")
                    print(f"Task Description:      {individual_task_view[2]} ")
                else:
                    print("You have no tasks assigned to you.")
                    break

      elif menu == 'sv':
        if(username=="admin"):
            print("Welcome to your statistics page")

            with open('tasks.txt', 'r+') as f:
                for line in f:
                    task_count = line
                    task_count_list.append(task_count)
 
            with open('user.txt', 'r+') as f:
                for line in f:
                    user_count = line
                    user_count_list.append(user_count)

            print(f"Total Number of tasks:           {len(task_count_list)} ")
            print(f"Total Number of users:           {len(user_count_list)} ")

        else:
            print("You do not have access to this")

      elif menu == 'e':
        print('Goodbye!!!')
        exit()

      else:
        print("You have made a wrong choice, Please Try again")