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


# Logic in Flow Chart explanation

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


# Existing Features

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


If instead, the day of the month chosen by the user is a valid one, the program will repeat it back and continue with asking for a particular time of that day.

![screenshot of valid date selected message and time of the day question](/assets/images/time_of_day.png)


A different message will be displayed to the user accordingly to his/her choice.

Morning message:

![screenshot of morning choice message](/assets/images/morning.png)

Afternoon message:

![screenshot of afternoon choice message](/assets/images/afternoon.png)

Evening message:

![screenshot of evening choice message](/assets/images/evening.png)

Night message:

![screenshot of night choice message](/assets/images/night.png)

Should the user write something else by mistake or intentionally, once again the program will ask to select one of the options listed.
![screenshot of invalid time of the day message](/assets/images/invalid_time_of_day.png)

Finally, the program will ask for the task info and it will show it back to the user once done writing

![screenshot of task info question](/assets/images/task_info.png)


A following option will ask the user if the task has to be saved

![screenshot of saving question](/assets/images/save_the_task.png)


If a negative answer will be given, then the program will check again what the user would like to do, and restart.

![screenshot of negative saving answer message](/assets/images/neg_saving.png)


If instead the user would like to indeed save the task, following messages will update the user of the saving progress.

![screenshot of saving progress message](/assets/images/saving_task.png)

At this point the file Agenda.csv will be updated with the user task, written underneath the selected day of the month.


Finally, the program will check if the user would like to do anything else. And it restarts again.

![screenshot of 'anything else' message](/assets/images/all_done_message.png)


Should the user select option 1 - Check your agenda , once again the program will make sure this option choice was intentional

![screenshot of selected option 1 message](/assets/images/option1_confirmation.png)


Once again it will check for the right input

![screenshot of valid input option 1 message](/assets/images/invalid_option1.png)


If the selection of option 1 or if the user has changed his/her mind, and doesn't want to check the agenda afterall, the program will display a message and once again the three initial options to choose from

![screenshot of different option to choose from](/assets/images/negative_option1.png)


If instead the user would really like to check the agenda,the loading progress will be displayed to inform the user of its progress and finally the agenda will get printed in the terminal. The task will be displayed underneath the right chosen day of the month - This is better shown in a csv file opened with Windows Excel, rather that in the terminal.

![screenshot of the agenda printed on the terminal](/assets/images/view_agenda.png)


In the example above the user originally selected day 2 from the calendar, so the task 'send email to Ellie' has been written on index[1] of the list... and so on.

At this point the program will inform the user that everything she/he asked has been done, and check if there is anything else to be done - here once again the three options will be displayed.

KINDLY NOTE: For the scenario in which the user select option 2, as a first option after starting the program, please see 'Fixed Problems & Testing' section of this readme file. 


Finally, should the user select option 3 - Exit Agenda , the program will check if this option is the correct one selected and if indeed the user would like to exit.

![screenshot of verification message for option 3](/assets/images/option3_verification.png)


Also here for any invalid options a message will be shown to the user, and the question will be fired again.

![screenshot of invalid option for option3](/assets/images/invalid.png)



If option 3 is not what the user would like to do, the program will aknowledge this and present the user with the three first options

![screenshot of negative exit option chosen](/assets/images/negative_exit.png)



If this was the intention of the user, some exiting progress messages will be displayed and the Agenda program will shut down, after a polite 'Bye' message.

![screenshot of exiting progress](/assets/images/exit_complete.png)


# Python libraries

To build this project some built in python libraries had been used, whilst others had been installed first.

Find a list below of the libraries I've imported, with some information about their purpose and usage.

- [Datetime](https://docs.python.org/3/library/datetime.html):
    -The datetime module supplies classes for manipulating dates and times.
- [Time](https://docs.python.org/3/library/time.html?highlight=time#module-time)
    - This module provides various time-related functions. I've been using it to add some second of program time sleep, to slow down its execution and give the user an impression of 'loading' or 'exiting' progressess.
- [Calendar](https://docs.python.org/3/library/calendar.html?highlight=calendar#module-calendar)
    - Used to display the actual calendar to the user.
- [Csv](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv) 
    -The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases. 


# Technologies used

Kindly, find below some of the technologies and websites used to complete this project. Follow the link to their websites to check them out if needed.

-   [W3Schools](https://www.w3schools.com/)
    - Used to check python language lessons and find solutions to some bugs.
-   [Python](https://www.python.org/)
    - Used to elaborate some python concepts.    
-   [Youtube](https://www.youtube.com/)
    - Used to check some tutorials about python language and overall to have an idea of what I could have done as a project. 
-   [LucidChart](https://www.lucidchart.com/pages/)
    - Used to create the flow diagram to have a better idea of the program logic to follow.
-	[GitHub](https://github.com/)
	- Used to store code for the project after being pushed.
-	[Git](https://git-scm.com/)
	- Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-	[Gitpod](https://www.gitpod.io/)
	- Used as the development environment.
-	[Heroku](https://id.heroku.com/login)
    - Used to deploy my project.


# Fixed Problems & Testing

During the whole coding process I've been checking for any errors that could have interfered with the program running smoothly.

Many testing had to be run to double check the user inputs and their validity, or better said the invalid option chosen either by mistake or intentionally.

Minor problems have been fixed throughtout the coding , mainly about indentation and syntax.

The actual big issue I fixed with a simple solution presented itself in the scenario when the user, right after starting the program would choose 'option 1.

My initial idea was that the program, once running , would have created the 'Agenda.csv' file by itself, whilst the user selected the various options diplayed to him/her. 
However, in this case it would have meant that there was no file Agenda at all to check at the starting point of the program, and so, if the user were to select 'option 1 - Check the agenda' the program would have crushed.

This had been fixed by reverting into creating the file myself, and add a first line in it stating that the 'Agenda' is at this stage empty, and suggesting the user to select a different option before opting for this, followed by an empty line 2 to increase readability once printed in the terminal.

## -from file Agenda.csv
![screenshot of Agenda file](/assets/images/empty_agenda.png)

## -from the terminal
This is exactly what is then printed in the terminal, before presenting the user with the three initial options.

![screenshot of empty agenda message](/assets/images/empty_agenda_terminal.png)


# Validation