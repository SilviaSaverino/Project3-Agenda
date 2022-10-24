#Allows to save your data once you've done using this programm
import pickle

week = {'Monday: [] ,Tuesday: [], Wednesday: [], Thursday: [], Friday: [], Saturday:[], Sunday: []'}

def weekly_agenda():
    """
    Starts the programm asking the user what tasks would it like to be performed
    """
    choice = input('Welcome! What would you like me to do? Please, insert one of the following:\n 1 - Check your plans for the week. \n 2 - Create an event. \n 3 - Cancel event.\n')
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
    correct = input('You would like to check your agenda, correct? Y/N \n') #NoteTOSelf: must make sure also a lower N or Y will be fine
    if correct == 'Y':
        print('YES function \n')
    elif correct == 'N':
        print('Sure, select a different option \n')
        options()
    else:
        print('This options is not correct, please input "Y" for yes, and "N" for no \n')    
        # When the answer is not correct, the program will start again
        check_week()         


def options():
    print('Choose a different option:\n 1 - Check your plans for the week. \n 2 - Create an event. \n 3 - Cancel event.\n ')
    #NoteTOSelf: once here the user can not continue at the moment!

weekly_agenda()    