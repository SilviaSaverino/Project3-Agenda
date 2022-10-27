# Allows to save your data once you've done using this programm
import pickle
# Get and allows to display actual date and time
import datetime
# Allows to set a time interval of x seconds between operations and calendar will show a standard calendar
import time
import calendar

#import test



# from datetime
now = datetime.datetime.now()
print("Welcome! Current date and time:")
print(now.strftime("Today is %A, %Y-%m-%d %H:%M"))


# from calendar
c = calendar.TextCalendar(calendar.MONDAY)
future_date = c.formatmonth(2023, 1)
print('Welcome to your Agenda', future_date)

#Creates an array of 31 days with nested arrays ; index[1] of each index[0] for each of the 31 arrays,will be calling a function
daysList = [[] for x in range(31)]

def add_task(day, task_detail):
    """
    Runs through the daysList lists and assigns the task to the selected day
    """
    new_pos_task = len(daysList[day - 1])
    daysList[day - 1].append(new_pos_task, task_detail)


def write_task():
    """
    Ask the user to select a day and what it has to note down for that day.
    """
    day = input('Choose a day:')
    task_detail = input('Tell me your task for the day:')
    add_task(day, task_detail)



def weekly_agenda():
    """
    Starts the programm asking the which task will be execute
    """
    choice = input('What would you like to do? Please, insert one of the following:\n 1 - Check your plans for the week. \n 2 - Add an event. \n 3 - Cancel event.\n')
    if choice == '1':
        check_week()
    elif choice == '2':
        add_event()
        # insert function here
    elif choice == '3':
        print('hola')
        # insert function here
    else:
        print('Incorrect option. Your input must be a number from the list \n')   


def check_week():
    """
    Check if the user wants to check his/her agenda and runs 
    functions accordingly to Y or N choice.
    Runs only if the user select option 1.
    """
    correct = input('You would like to check your agenda, correct? Y/N \n').upper() 
    if correct == 'Y':
        print('Thank you. Loading agenda...')
        time.sleep(2)
        # add function to open the agenda here
        print('YES function \n')
    elif correct == 'N':
        print('Sure, select a different option \n')
        weekly_agenda()
    else:
        print('Incorrect option. Input "Y" for yes, or "N" for no \n')    
        # When the answer is not correct, the program will start again
        check_week()         


def add_event():
    """
    Check if the user wants to add a task in his/her agenda and runs 
    functions accordingly to Y or N choice.
    Runs only if the user select option 2.
    """
    add = input('You would like to add an event in your agenda, correct? Y/N \n').upper() 
    if add == 'Y':
        print('Thank you. Loading agenda...')
        time.sleep(2)
        # add function to open the agenda here
        print('YES function \n')
    elif add == 'N':
        print('Sure, select a different option \n')
        weekly_agenda()
    else:
        print('Incorrect option. Input "Y" for yes, or "N" for no \n')    
        # When the answer is not correct, the program will start again
        check_week()         


weekly_agenda()  

