#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs
daysList = [[] for x in range(31)]
 

list_length = 3

task = input('time?')
day = input('when?')
cosa = input('prova')

for idx in range(list_length):
    item = [task, day, cosa]
    daysList.append(item)

def check_week():
    """
    Check if the user wants to check his/her agenda and runs 
    functions accordingly to Y or N choice.
    Runs when the user select option 1.
    """
    while True:
        correct = input('Check your agenda, correct? Y/N \n').upper() 
        daysList.append(correct)
        if correct == 'Y':
            print('Thank you. Loading agenda...')
            #time.sleep(1.5)
            # add function to open the agenda here
            print('YES function \n')
            return
        elif correct == 'N':
            print('Sure, select a different option \n')
            return
        else:
            print('Incorrect option. Input "Y" for yes, or "N" for no \n')    
            # When the answer is not correct, the program will start again

check_week()



print(daysList) 

'''
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
'''

