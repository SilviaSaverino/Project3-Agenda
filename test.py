#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs

print('CIAO')
daysList = [[] for x in range(31)]


def write_task():
    day = input('Choose a day:')
    task_detail = input('Tell me your task for the day:')
    add_task(day, task_detail)


def add_task(day, task_detail):
    new_pos_task = len(daysList[day - 1])
    daysList[day - 1].append(new_pos_task, task_detail)



