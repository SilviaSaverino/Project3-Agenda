# Project 3
# Agenda

'Agenda' is a small project built using Python language. This program will allow users to add, read, or cancel events and tasks from his Agenda.csv files.

 

# Intention:

Please note that this project is for Code Institute. It is to display some of the knowledge I acquired while studying the Python module.

## Main goals for this project are: 
-	To provide explicit instruction to the user, to let him/her follow the program flow intuitively
-	To update a csv file, 'Agenda'

# How It Works

The program will welcome the user, and an initial question will check the user's intentions. Depending on the option selected, the program will let the user:

 1) Open the csv file to display the agenda to the user and display the events in the terminal.
 2) Add a new task in their agenda, and update the file csv only if the user decides to save the event.
 3) Clear a task that no longer the user needs/wishes to perform on the specific date.

The program will run until the user decides to shut it down by selecting the exit option.


# UX

## Strategy:

'Agenda' allows the user to plan his weeks ahead of time and remind him/herself of the events/tasks of the month by letting her/him check the agenda.

No graphic is in this project, following directions of the passing criteria and deployment through Heroku.

## User Stories:

-	As a user, I would like to create an event for the agenda quickly
-   Save such event, displayed on the date of its occurrence
-   Receive explicit instruction if the command given is not correct
-   Exit the agenda once I have done with what I wanted to do


The stories goals above are reached by:
-	Let the user choose the initial task to perform once the program starts.
-   Let the user decide if the task written will be saved or not in the agenda file.
-   Displaying clear options for the user to choose from and promptly reminding or suggesting the correct input to continue the  program
-   Providing the user with an exit option


# Logic

Prior to jumping into coding, a draft of a flow diagram was manually written down simply to have a better idea of how the program would have run. Along with which steps of the program would have allowed the user to continue and what option chosen would have let the program start again or perform other options accordingly.

A final flow diagram was later created and added here below to show the steps/logic followed.


I’ve created the below diagram through [Lucid Chart](https://www.lucidchart.com/pages/) website 


The free version of tools offered once creating an account was good enough for this purpose.

Find below the flow chart followed to create this program.

![Lucid Chart flow diagram image](/assets/images/lucid_chart.png)


# Logic in Flow Chart explanation

The user will be welcomed into the Agenda program and promptly informed of the date and time of the day.

Three options are presented to the user:
 
- 1) Check agenda
- 2) Add Event
- 3) Exit Agenda

Should the user select option 1 - Check agenda, the program will print the current agenda file on the terminal and ask the user if she/he would like to exit the program. With a positive answer, the program will update the user with the exiting progress and shut down the program with some greetings. With a negative answer, the program will check what else the user would like to do and show he/she the three initial options again.

Should the user select option 2 - Add event, the program will show the user a mini calendar - in this version showing the month of Jan 2023 - the program will then ask the user to select a day from the calendar. If a correct option is not selected, the program will prompt the user with an answer to keep on running. If a correct option is given, the program will ask for a time of the day when the user is more likely to perform such a task/event. Once again, the program will check whether a valid option is given. If not, once again will prompt the user with a valid answer; if yes, the program will ask for the task information. Once the user provides such information, the program will print it back and check if the user would like to save such a task or now. If not, the program will check if the user would like to exit the program; if yes, the program will update the user with the saving progress and, once done, will check if the user would like to exit.

Should the user select option 3 - Exit Agenda, the program will double-check if the user would like to exit, and if so, it will update the user with the exiting progress until the program shuts down and greet the user. If, instead, the user would like not to exit, the program will present the user with the three initial options to check what else she/he would like to do. 


# Existing Features

In this agenda release, the program is at its simplest version.

A polite welcome will be displayed as soon as the user runs the program, stating the current date and time.

![screenshot of welcoming message](/assets/images/welcoming.png)



The user will be then presented with three options to check what she/he would like to do

![screenshot of user options to choose from](/assets/images/options.png)


Should the user select an option not listed, the program will remind/suggest to the user that she/he must choose and insert a number from the list.

![screenshot of incorrect option selected message](/assets/images/invalid_option123.png)


Should the user select option 2 - Add event. The program will check if this option was intentionally selected and, if so will update the user with the loading progress and print a calendar (kindly note in this initial release, the calendar set on Jan 2023)

![screenshot of option chosen checking](/assets/images/add_event_option.png)


![screenshot of the calendar](/assets/images/loading.png)


Here the user will be asked to choose a day of the month.

![screenshot of message asking to pick a day of the month](/assets/images/choosing_day.png)


If the day is not within any calendar date, the program will prompt the user to select a valid option.

![screenshot of not valid date message](/assets/images/wrong_day.png)


If instead, the day of the month chosen by the user is a valid one, the program will repeat it back and continue asking for a particular time of that day.

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


Should the user write something else by mistake or intentionally, the program will again ask to select one of the options listed.

![screenshot of invalid time of the day message](/assets/images/invalid_time_of_day.png)


Finally, the program will ask for the task info, and it will show it back to the user once done writing.

![screenshot of task info question](/assets/images/task_info.png)


The following option will ask the user if the task is to save.

![screenshot of saving question](/assets/images/save_the_task.png)


If a negative answer is given, the program will check what the user would like to do again and restart.

![screenshot of negative saving answer message](/assets/images/neg_saving.png)


If the user would like to save the task, the following messages will update the user on the saving progress.

![screenshot of saving progress message](/assets/images/saving_task.png)

At this point, the file Agenda.csv will be updated with the user task, written underneath the selected day of the month.


Finally, the program will check if the user wants to do anything else. Furthermore, it restarts again.

![screenshot of 'anything else' message](/assets/images/all_done_message.png)


Should the user select option 1 - Check agenda, once again, the program will ensure this option choice was intentional.

![screenshot of selected option 1 message](/assets/images/option1_confirmation.png)


Once again, it will check for the correct input.

![screenshot of valid input option 1 message](/assets/images/invalid_option1.png)


If the selection of option 1 or if the user has changed their mind, and does not want to check the agenda afterwards, the program will display a message.

![screenshot of different option to choose from](/assets/images/negative_option1.png)


If, instead, the user would like to check the agenda, the loading progress will be displayed to inform the user of its progress, and finally, the agenda will get printed in the terminal. The task will be displayed underneath the right chosen day of the month - This is better shown in a csv file opened with Windows Excel, rather than in the terminal.

![screenshot of the agenda printed on the terminal](/assets/images/view_agenda.png)


In the example above the user originally selected day 2 from the calendar, so the task 'send email to Ellie' has been written on index[1] of the list... and so on.

At this point, the program will inform the user that everything she/he asked has been done and check if there is anything else to be done - here, once again, the three options will be displayed.

KINDLY NOTE: For the scenario in which the user selects option 2, as the first option after starting the program, please see the 'Fixed Problems & Testing' section of this readme file.


Finally, should the user select option 3 - Exit Agenda, the program will check if this option is the correct one and if the user would like to exit.

![screenshot of verification message for option 3](/assets/images/option3_verification.png)


Also, a message will display to the user for invalid options, and the question will repeat.

![screenshot of invalid option for option3](/assets/images/invalid.png)



If option 3 is not what the user would like to do, the program will acknowledge this and present the user with the first three options.

![screenshot of negative exit option chosen](/assets/images/negative_exit.png)



If this were the user's intention, some exit progress messages would be displayed, and the Agenda program will shut down after a polite 'Bye' message.

![screenshot of exiting progress](/assets/images/exit_complete.png)


# Python libraries

Please find a list below of the libraries I have imported, with some information about their purpose and usage.

- [Datetime](https://docs.python.org/3/library/datetime.html):
    -The datetime module supplies classes for manipulating dates and times.
- [Time](https://docs.python.org/3/library/time.html?highlight=time#module-time)
    - This module provides various time-related functions. I've been using it to add some second of program time sleep, to slow down its execution and give the user an impression of 'loading' or 'exiting' progressess.
- [Calendar](https://docs.python.org/3/library/calendar.html?highlight=calendar#module-calendar)
    - Used to display the actual calendar to the user.
- [Csv](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv) 
    -The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases. 


# Technologies used

Below are some of the technologies and websites used to complete this project. Follow the link to their websites to check them out if needed.

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

During the coding process, I have been checking for any errors that could have interfered with the program running smoothly.

Many testing had to be run to double-check the user inputs and their validity, or better said, the invalid option was chosen either by mistake or intentionally.

Minor problems have been fixed throughout the coding, mainly with indentation and syntax.

The actual big issue I fixed with a simple solution presented itself in the scenario when the user, right after starting the program, would choose 'option 1.

The initial idea was that the program, once running, would have created the 'agenda.csv' file by itself whilst the user selected the various options displayed to him/her.

However, in this case, it would have meant that there was no file Agenda to check at the starting point of the program, and so, if the user were to select 'option 1 - Check the agenda', the program would have crushed. 

This had been fixed by reverting to creating the file myself and adding the first line in it stating that the 'Agenda' is at this stage empty and suggesting the user select a different option before opting for this, followed by an empty line 2 to increase readability once printed in the terminal.

![screenshot of Agenda file](/assets/images/empty_agenda.png)


![screenshot of empty agenda message](/assets/images/empty_agenda_terminal.png)


# Validation
Validation was done using PEP8 and the Black library online as shown in image
![screenshot of validation PEP8](/assets/images/validation.png)

# Deployment

I follow these steps to deploy my project.

See below for the Github procedure, and further down for the Heroku one.

## Github

### Forking the GitHub repository
To view and edit the code without affecting the original repository:
•	Locate the GitHub repository.
•	Click on Fork, in the top right-hand corner.
•	This will take you to your own repository to a fork with the same name as the original branch.


### Creating a local clone of your project
•	Go to the GitHub repository. 
•	Click on Code to the right of the screen, click on HTTPs and copy the link.
•	Open Git Bash and change the current working directory to the location where you want the cloned directory.
•	Type git clone, paste the URL you copied earlier, and press Enter to create your local clone.

## Heroku


# Credits

## Content
The content of this program has been created by the owner and all of the questions either in form of input or print similar to any other question asked by a different program is purely coincidental.

## Acknowledgements

The following people who had been helpful and supportive during the creation of 'Agenda.'

- Francesco Rubino
- Spencer Barriball
- Martina and Cosimo Toppi
- The Slack community of 'Code Institute' ~ in particular Harry Dhillon for his prompt replies and great tips
