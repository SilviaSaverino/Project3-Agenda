#Allows to save your data once you've done using this programm
import pickle
#Get and allows to display actual date and time
import datetime
#Allows to set a time interval of x seconds between operations
import time
import calendar

#from datetime
now = datetime.datetime.now()
print ("Welcome! Current date and time:")
print (now.strftime("Today is %A, %Y-%m-%d %H:%M"))


#from calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2023,1)
print('Welcome to your Agenda' , str)

week = {'Monday: [] ,Tuesday: [], Wednesday: [], Thursday: [], Friday: [], Saturday:[], Sunday: []'}

def weekly_agenda():
    """
    Starts the programm asking the user what tasks would it like to be performed
    """
    choice = input('What would you like to do? Please, insert one of the following:\n 1 - Check your plans for the week. \n 2 - Create an event. \n 3 - Cancel event.\n')
    if choice == '1':
        check_week()
    elif choice == '2':
        print('ciao')
        #insert function here
    elif choice ==  '3':
        print('hola')
        #insert function here
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
        #add function to open the agenda here
        print('YES function \n')
    elif correct == 'N':
        print('Sure, select a different option \n')
        weekly_agenda()
    else:
        print('This options is not correct, please input "Y" for yes, and "N" for no \n')    
        # When the answer is not correct, the program will start again
        check_week()         

weekly_agenda()    