# Project 3
# Agenda

'Agenda’ is a small project built using Python language. This program will allow the user to add, read, or cancel event and tasks from his Agenda.csv files

INSERT PIC FROM AM I RESPONSIVE HERE

 

# Intention:

Please note this project had been built purely as my Third Project for Code Institute Course. It is simply a display of some of the knowledge I've acquired whilst studying Python module.

## Main goals for this project are: 
-	To provide clear instruction to the user, to let him/her follow the program flow intuitively
-	To create and update a csv file ‘Agenda’

# How It Works

The user will be welcomed by the program and an initial question will be fired to check the user intentions.
Depending on the option selected, the program will let the user:

 1) Open the csv file to display the Agenda to the user, and also display the events in the terminal.
 2) Add a new task in his agenda, and update the file csv only if the user decides to save the event.
 3) Clear a task that no longer the user need/wish to perform on the specific date.

The program will run, until the user decides to shut it down, by selecting the exit option.


# UX

## Strategy:

'Agenda’ had been created with the intention of allowing the user to plan his weeks ahead of time and remind him/herself of the events/tasks of the month, by letting her/him check the agenda.

No graphic had been added to this project, following directions of the passing criteria, and to allow deployment through Heroku.

## User Stories:

-	As an user I would like to easily create an event for my agenda
-	Save such event, displayed on the date of its occurrence
-	Receive clear instruction if the command given are not correct
-   Exit the Agenda once I've done with what I wanted to do

The stories goals above are reached by:
-	Let the user choose the initial task to perform once the program starts
-	Let the user decide if the task written will be saved or not in the agenda file
-	Displaying clear options for the user to choose from, and promptly remind or suggest the right input to continue the program
-   By providing the user with an exit option

# Website Design

No design had been added to this version of the project. My understanding of the instruction given by Code Institute is that no graphic libraries can be used to allow deployment through Heroku.


# Logic

Prior to jumping into coding, a draft of a flow diagram was manually written down, simply to have a better idea of how the program would have run, which steps of the program would have allow the user to continue and what option chosen would have let the program start again, or perform other options accordingly.

A final flow diagram, was later created and added here below to show the steps/logic followed. 

I’ve created the below diagram through [Lucid Chart](https://www.lucidchart.com/pages/) website 


I’ve found that the free version of tools offered once creating an account, was good enough for this purpose. 

Kindly, find below the flow chart followed to create this program.

![Lucid Chart flow diagram image](/assets/images/lucid_chart.png)


## Explain Logic in Flow Chart

The user will be welcomed in the Agenda program, and promptly informed with the date and time of the day.

Three options will be presented to the user: 
- 1) Check agenda
- 2) Add Event
- 3) Exit Agenda

Should the user select options number 1 - Check Agenda, the program will simply print the current agenda file on the terminal, and ask the user if she/he would like to exit the program. 
With a positive answer the program will update the user with the exiting progress and shut down the program with some greetings of sorts.
With a negative answer the program will check what else the user would like to do, and show he/she the three initial options again.

Should the user select option 2 - Add event, the program will show the user a mini calendar - in this version showing the month of Jan 2023 - the program will then ask the user to select a day from the calendar. If a correct option is not selected, the program will prompt the user with an answer to keep on running. If a correct option is given, then the program will ask for a time of the day when the user is more likely to perform such task/event. Once again the program will check if a valid option is given or not. If not, once again will prompt the user with a valid answer; if yes, the program will ask for the task information.
Once the user provide such information, the program will print it back and check if the user would like to save such a task or now. If not, the program will check if the user would like to exit the program; if yes the program will update the user with the saving progress and once done will check if the user would like to exit.

Should the user select option 3 - Exit Agenda, the program will double check if the user would like to exit, and if so it will update the user with the exiting progress until the program shut down and greet the user; if instead the user would like not to exit, the program will present the user with the three initial options, to check what else she/he would like to do. 


## Existing Features

In this release of Agenda, the program is on its simplest version.

A polite welcome will be displayed as soon as the user runs the program, stating also the current date and time.

![screenshot of welcoming message](/assets/images/welcoming.png)



The user will be then presented with three options, to check what she/he would like to do

![screenshot of user options to choose from](/assets/images/options.png)


Should the user select an option not listed, the program will remind/suggest the user that she/he must choose and insert a number from the list.

![screenshot of incorrect option selected message](/assets/images/invalid_option123.png)


Should the user select option 2 - Add event. The program will check if this option was intentionally selected and if so will update the user with the loading progress and print a calendar (kindly note in this initial release the calendar is set on Jan 2023)

![screenshot of option chosen checking](/assets/images/add_event_option.png)


![screenshot of the calendar](/assets/images/loading.png)


Here the user will be asked to choose a day of the month

![screenshot of message asking to pick a day of the month](/assets/images/choosing_day.png)

If the day is not within any date in the calendar, once again the program will prompt the user to select a valid option.

![screenshot of not valid date message](/assets/images/wrong_day.png)

If instead, the day of the month chosen by the user was a valid one, the program will repeat it back and continue with asking for a particular time of that day.

![screenshot of valid date selected message and time of the day question](/assets/images/repeat_chosen_day.png)