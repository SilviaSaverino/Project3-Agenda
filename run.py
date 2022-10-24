#Allows to save your data once you've done using this programm
import pickle

week = {'Monday: [] ,Tuesday: [], Wednesday: [], Thursday: [], Friday: [],Saturday:[], Sunday: []'}
print(week)

def weekly_agenda():
    """
    Starts the programm asking the user what tasks would it like to be performed
    """
    choice = input('Welcome! What would you like me to do? Please, insert one of the following:\n 1 - check your plans for the week. \n 2 - create an event. \n 3 - to cancel event.\n')
    print(choice)
    if choice == '1':
        print(hello)
        #examine_week()
    elif choice == '2':
        print(ciao)
        #insert function here
    elif choice ==  '3':
        print(hola)
        #insert function here
    else:
        print('Incorrect option. please select an option from this list: \n 1 - check your plans for the week. \n 2 - create an event. \n 3 - to cancel event.\n')   


weekly_agenda()

