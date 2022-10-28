#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs

print('CIAO')
daysList = [[] for x in range(31)]

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

morning_choice = 'From 7:00 to 12:00'
afternoon_choice = 'From 12:00 to 18:00'
evening_choice = 'From 18:00 to 23:00'
night_choice = 'You deserve some sleep! Select a different time of the day.'

def write_task():
    day = str(input('Choose a day of the week:\n').capitalize())
    if day in week_days:
        print(f'{day} sounds like a good day!\n') #write the part to append it into the file!
    else:
        print(f'Sadly {day} is not a day of the week:\n')
        write_task()
        time.sleep(1)

    #deve finire qui? break or continue? not sure at the moment
    task_detail = input(str('What is your task?\n'))  
    print('Adding this task in your Agenda\n')

    #funzione per inserire dati nel file!

    

    time = str(input('Any particular time of the day?').lower())
    if time == Morning:
        print('You should do this')
    

    
    

    add_task(day, task_detail)


def add_task(day, task_detail):
    new_pos_task = len(daysList[day - 1])
    daysList[day - 1].append(new_pos_task, task_detail)


write_task()
