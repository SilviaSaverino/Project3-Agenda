# Allows to save your data once you've done using this programm
import pickle
# Get and allows to display actual date and time
import datetime
# Allows to set a time interval of x seconds between operations and 
# calendar will show a standard calendar
import time
import calendar

import csv
###
# Costants and Global variables
###
# from datetime
now = datetime.datetime.now()

# Creates an array of 31 days with nested arrays ; index[1] of each index[0] 
# for each of the 31 arrays,will be calling a function
daysList = [[] for x in range(31)]
firstRow = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

# Below some time of the day options for the user to chose from
MORNING = 'anytime from 7:00 to 12:00 '
AFTERNOON = 'anytime from 12:00 to 18:00 '
EVENING = 'anytime from 18:00 to 23:00 '
NIGHT = 'You deserve some sleep! Select a different time of the day.'


###
# Functions
###
def weekly_agenda():
    """
    Starts the programm asking which task will be executed
    """
    while True:
        print('What would you like to do? Insert one of the following:\n')
        choice = input('1-Check your Agenda.\n2-Add event.\n3-Cancel event.\n')
        if choice == '1' or choice == '2' or choice == '3':
            return choice
        print('Incorrect option. Your input must be a number from the list \n')


def check_week():
    """
    Check if the user wants to check his/her agenda and runs 
    functions accordingly to Y or N choice.
    Runs when the user select option 1.
    """
    while True:
        correct = input('Check your agenda, correct? Y/N \n').upper() 
        if correct == 'Y':
            print('Thank you. Loading agenda...\n')
            time.sleep(1.5)
            # add function to open the agenda here
            read_file()
            exit_program()
            break
        if correct == 'N':
            print('Sure, select a different option \n')
            return
        print('Incorrect option. Input "Y" for yes, or "N" for no \n')  
        # When the answer is not correct, the program will start again


def read_file():
    '''
    Open the csv.file
    '''
    with open('testing.csv', 'r') as file:
        reader = csv.reader(file)
        print(file.read())
        file.close()  


def exit_program():
    '''
    Exit the program if the user would like to do so.
    '''
    print('Loading complete.\n')
    exiting = str(input('Would you like to exit the Agenda? Y/N\n')).upper()
    while True:
        if exiting == 'Y':
            print('Closing the Agenda...\n')
            time.sleep(1)
            print('Agenda closed. Bye!')
            exit()
        if exiting == 'N':
            weekly_agenda()     ############################# ASK SPENCER! the code once here doesn't run! ##################
        print('Incorrect option\n')
        return ####### my brain! this is restarting eveything! I want to restart this function only! #########
 

def show_calendar():
    """
    Shows an actual calendar to the user, for a better user experience.
    """
    c = calendar.TextCalendar(calendar.MONDAY)
    future_date = c.formatmonth(2023, 1)
    print('Calendar', future_date)


def request_day():
    """
    Ask the user to select a day and what it has to note down for that day.
    """
    show_calendar()
    while True:
        day = int(input('Choose a day of the month:\n'))
        if day in range(len(daysList)):
            print(f'{day} sounds like a good day!\n')
            return day 
        print(f'Sadly {day} is not a valid option:\n')


def request_time():
    """
    Ask the user if she/he would like to perform her/his task during
    the morning, afternoon, evening or at night.
    """
    while True:
        time = str(input('Any particular time of the day?\n').upper())
        if time == 'MORNING':
            print('You should do this between', MORNING)
            return MORNING
        if time == 'AFTERNOON':
            print('You should do this between', AFTERNOON)
            return AFTERNOON
        if time == 'EVENING':
            print('You should do this between', EVENING)
            return EVENING
        if time == 'NIGHT':
            print('At night?', NIGHT)
            # Not tasks will be done at night, this function will run again
        print('When again? Morning, afternoon, evening or night?\n')
        # When the answer is not correct, this function will run again


def request_task():
    """
    Ask the user to write the task of the day and 
    """
    task_detail = input(str('What is your task?\n'))  
    print(f'Adding "{task_detail}" in your Agenda\n')
    return task_detail            


def save_task(day, day_span, task_detail):
    """
    Save task under the right day/header.
    """
    while True:
        saving = input(str('Would you like to save this task? Y/N \n')).upper()
        if saving == 'Y':
            print('Cool. Saving your task')
            time.sleep(1)
            daysList[day - 1].append(day_span+'your task is to: '+task_detail)
            print('All done. Task saved.')
            print(daysList)

            return
        if saving == 'N':
            print('Okay then. Have a great day')
            return

        print('Invalid option. Type Y for yes, N for no')    


def file_creation():
    '''
    Create file csv to store user inputs
    '''
    with open('testing.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(firstRow)
        writer.writerow(daysList)


def add_event():
    """
    Check if the user wants to add a task in his/her agenda and runs 
    functions accordingly to Y or N choice.
    Runs when the user select option 2.
    """
    while True:
        add = input('Add an event in your agenda, correct? Y/N \n').upper() 
        if add == 'Y':
            print('Thank you. Loading agenda...\n')
            time.sleep(1.5)
            day = request_day()
            time.sleep(0.5)
            day_span = request_time()
            task_info = request_task()
            # saving function below
            save_task(day, day_span, task_info)
            file_creation()

            return
        if add == 'N':
            print('Sure, select a different option \n')
            return
        print('Incorrect option. Input "Y" for yes, or "N" for no \n')    
        # When the answer is not correct, the program will start again


###
# Entry point
###
print("Welcome to your Agenda\n")
print(now.strftime("Today is %A, %Y-%m-%d %H:%M \n"))

while True:
    # Ask for an operation
    oper_selected = weekly_agenda()

    if (oper_selected == '1'):
        check_week()
    elif (oper_selected == '2'):
        add_event()    
    elif (oper_selected == '3'):
        print('hola')
        break
        # insert function here
