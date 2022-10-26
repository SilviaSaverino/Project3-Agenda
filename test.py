#File created to write block of code singularly and test them, before adding them into the run.py file. 
#To be deleted before submitting the project.abs

print('CIAO')

def days():
    global day
    day = input("Which day? ").capitalize()
    week_list = [day_list for day_list in week.keys()]
    if day not in week_list:
        print("Invalid day.")
        days()