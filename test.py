#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs

print('CIAO')
daysList = [[] for x in range(31)]

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

# funzione per sapere di quale task si tratta. 
    
       

task_info()


def continue_or_exit():
    """
    Check if the user would like to continue the program, or exit it
    """
    print('Would you like to continue or exit the Agenda?\n')
    continue_exit = input(str('Select C to continue, or E to exit the Agenda')).upper()
    if continue_exit == 'C':
        print("Let's add one more task then.\n")
        task_info()
    elif continue_exit == 'E':
        print('Exiting...')
        time.sleep(1)
        print('Program terminated. Have a great day!')  
        # add function to exit the program  
    else:
        print('Incorrect option. Try again.')
        continue_or_exit()    # is this going to work? check!        
   
def save_edit():
    """
    Check if the user would like to save the task in the
    file.csv and continue accordingly to the user choice.
    """   
    saving_edit = input(str('Select S for saving, or M to Modify task\n')).upper()
    if saving_edit == 'S':
        print('Great! Saving task...\n')
        time.sleep(1)
        add_task(day, task_detail)
        print('Saved. Would you like to continue or exit?\n')
        continue_or_exit()
    elif saving_edit == 'M':
        print('Sure, what would you like to change?\n')
        # another function here.
    else:
        print('Not a correct option\n')
    save_edit() 

#add_task(day, task_detail)






def create_file():
    """
    Create a file.csv with the days in the months as header
    """
    with open('YourAgenda.csv', 'w') as f:
        header = [1,2,3,4,5,6,7,8,9,10,
        11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
       
  
    
def add_task(day, task_detail):
    """
    Add the user task below the right header, 
    the latter reprensenting the day of the month
    previously chosen by the user.
    """
    new_pos_task = len(daysList[day - 1])
    daysList[day - 1].append(new_pos_task, task_detail)


