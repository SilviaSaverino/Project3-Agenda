# Allows to save your data once you've done using this programm
import pickle
# Get and allows to display actual date and time
import datetime
# Allows to set a time interval of x seconds between operations and 
# calendar will show a standard calendar
import time
import calendar


# from datetime
now = datetime.datetime.now()
print("Welcome to your Agenda\n")
print(now.strftime("Today is %A, %Y-%m-%d %H:%M \n"))


# from calendar
def show_calendar():
    """
    Shows an actual calendar to the user, for a better user experience.
    """
    c = calendar.TextCalendar(calendar.MONDAY)
    future_date = c.formatmonth(2023, 1)
    print('Calendar', future_date)


# Creates an array of 31 days with nested arrays ; index[1] of each index[0] 
# for each of the 31 arrays,will be calling a function
daysList = [[] for x in range(31)]

#Below some time of the day options for the user
MORNING = 'anytime from 7:00 to 12:00\n'
AFTERNOON = 'anytime from 12:00 to 18:00\n'
EVENING = 'anytime from 18:00 to 23:00\n'
NIGHT = 'You deserve some sleep! Select a different time of the day.\n'


def add_task(day, task_detail):
    """
    Runs through the daysList lists and assigns the task to the selected day
    """
    new_pos_task = len(daysList[day - 1])
    daysList[day - 1].append(new_pos_task, task_detail)


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
    Runs when the user select option 1.
    """
    correct = input('Check your agenda, correct? Y/N \n').upper() 
    if correct == 'Y':
        print('Thank you. Loading agenda...')
        time.sleep(1.5)
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
    Runs when the user select option 2.
    """
    add = input('Add an event in your agenda, correct? Y/N \n').upper() 
    if add == 'Y':
        print('Thank you. Loading agenda...\n')
        time.sleep(1.5)
        show_calendar()
        time.sleep(0.5)
        write_task()
        
    elif add == 'N':
        print('Sure, select a different option \n')
        weekly_agenda()
    else:
        print('Incorrect option. Input "Y" for yes, or "N" for no \n')    
        # When the answer is not correct, the program will start again
        check_week()         


def write_task():
    """
    Ask the user to select a day and what it has to note down for that day.
    """
    day = int(input('Choose a day of the month:\n'))
    if day in range(len(daysList)):
        print(f'{day} sounds like a good day!\n')
        time_of_the_day() 
    else:
        print(f'Sadly {day} is not a valid option:\n')
        write_task()
        time.sleep(1)
    add_task(day, task_detail)


def time_of_the_day():
    """
    Ask the user if she/he would like to perform her/his task during
    the morning, afternoon, evening or at night.
    """
    time = str(input('Any particular time of the day?\n').upper())
    if time == 'MORNING':
        print('You should do this between', MORNING)
    elif time == 'AFTERNOON':
        print('You should do this between', AFTERNOON)
    elif time == 'EVENING':
        print('You should do this between', EVENING)
    elif time == 'NIGHT':
        print('At night?', NIGHT)
    else:
        print('When again? Morning, afternoon, evening or night?\n')
        time_of_the_day()  # not sure why this doesn't run...


weekly_agenda()  

