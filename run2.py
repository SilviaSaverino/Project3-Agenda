# Allows to save your data once you've done using this programm
import pickle
# Get and allows to display actual date and time
import datetime
# Allows to set a time interval of x seconds between operations and 
# calendar will show a standard calendar
import time
import calendar


# from datetime
now = datetime.datetime.now()

###
#Costants and Global variables
###

# Creates an array of 31 days with nested arrays ; index[1] of each index[0] 
# for each of the 31 arrays,will be calling a function
daysList = [[] for x in range(31)]

# Below some time of the day options for the user to chose from
MORNING = 'anytime from 7:00 to 12:00\n'
AFTERNOON = 'anytime from 12:00 to 18:00\n'
EVENING = 'anytime from 18:00 to 23:00\n'
NIGHT = 'You deserve some sleep! Select a different time of the day.\n'

###
# Entry point
###
print("Welcome to your Agenda\n")
print(now.strftime("Today is %A, %Y-%m-%d %H:%M \n"))

###
# Functions
###