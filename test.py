#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs

print('CIAO')


def add_event():
    day = input('Choose a day:')
    taskDetail = input('Tell me your task for the day:')
    add_task(day, taskDetail)



def add_task(day, taskDetail):
    newPosTask = len(daysList[day - 1])
    daysList[day - 1].append(newPosTask, taskDetail)



