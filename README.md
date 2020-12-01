# zoomBot
A bot in the making to join my zoom classes

Currently in order to enter my zoom classes, I need to login through 
my schools canvas page and navigate to the zoom class. Right now, the
bot isnt able to differenciate which class I need to be in based on day
or time. 
I plan to put that in when next semester rolls around

The bot asks which class I need to be in, then logs me into canvas, and 
navigates to the correct zoom class

`````````````````````````````````````````````````````````````````````````````````````````````

Update 11/26/2020:
-revised to add .txt processing
-now checks users day of week and time
  compares user day of week and time 
  with .txt info
-Added initial setup
  initial setup creates new 
  .txt with class info from user

When user first runs the bot, it checkks if classes.txt exists in its directory
If not, it creates a new classes.txt and asks for the name, day of week, 
  start time, and zoom url for each class
If classes.txt exists, the bot iterates through the file lookking for matching
  day of week and start time of users computer
When it finds matching day and time, it takkes the url in the next line and opens 
  the zoom link as well as canvas.instructure

`````````````````````````````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````````````````````

Update 11/29/2020:
-Updated openClass() function

openClass() now updates the current day and time, then rechecks the .txt again until the 
  a matching class is found to open

`````````````````````````````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````````````````````

Update 11/30/2020:
-Canvas page no longer hard coded
-User now inputs their canvase home page during initial setup

Before, the canvas page was hard coded, with no way to change it, so it always went to IU
Now, the user can input their own canvas page during the setup. The bot then checks the .txt
  for the canvas link (looks for the key word "instructure"), then sends the link to the 
  canvasLogin() function
  
`````````````````````````````````````````````````````````````````````````````````````````````
