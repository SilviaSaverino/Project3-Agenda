#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs

print('CIAO')
daysList = [[] for x in range(31)]

MORNING = 'anytime from 7:00 to 12:00\n'
AFTERNOON = 'anytime from 12:00 to 18:00\n'
EVENING = 'anytime from 18:00 to 23:00\n'
NIGHT = 'You deserve some sleep! Select a different time of the day.\n'


def write_task():
    day = int(input('Choose a day of the month:\n'))
    if day in range(len(daysList)):
        print(f'{day} sounds like a good day!\n') 
    else:
        print(f'Sadly {day} is not a valid option:\n')
        write_task()
        time.sleep(1)
    time_of_the_day()


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
    time_of_the_day()


    #chiamare funzione qui.

    #deve finire qui? break or continue? not sure at the moment
   # task_detail = input(str('What is your task?\n'))  
   # print('Adding this task in your Agenda\n')

    #funzione per inserire dati nel file!

    
  
    

#add_task(day, task_detail)



write_task()


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


#def edit_task_in_file() #rimuovere or edit?