#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs

print('CIAO')

daysList = [[] for x in range(3)]

for d in daysList:
    d.insert(0, 'Task')

daysList[2].insert(1,'New Task')

print(daysList)