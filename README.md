# zoomBot
A bot in the making to join my zoom classes

For your own use, download the zoomBotAdvanced.py
Day of week must be full name i.e. Monday, Tuesday...
Start Time must be in 24 hour clockk i.e. 17:30

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
`````````````````````````````````````````````````````````````````````````````````````````````

Update 12/1/2020:
-Added username/password support
-Bot no longer assumes user/pass is saved and autofilled

Before, the bot would assume the browser saved the user/pass, so it would just click autofill
Now the user specifies a username and password in setup, then the bot types them when opening canvas

`````````````````````````````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````````````````````

Update 01/07/2021:

-Tweaked canvasLogin() function for duo verification
-Added clarification for setup()

Previously, the bot relied on the user being in full screen mode and having the same screen dimensions
as the creator. Now the bot tabs over to the button and presses enter, more accessable to users
Also added more clarification for the setup so users kknow what the bot looks for when checking day and time

`````````````````````````````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````````````````````
Update 01/21/2021:
-openZoom() no longer moves to preprogrammed coordinates

Previously when opening zoom, the openZoom() functionwould go to preprogrammed coordinates.
Now the function detirmines user screen size, calculates the desired position, and moves there.



