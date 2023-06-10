 Name: 		Give Points<br />
 Version: 	4.20.69<br />
 Creator: 	zmotan<br />
 Website:	https://zmotan.com<br />
<br />
Simple yet most reliable script for transfering points between users on Youtube.

Template: 	<br />
"[command] [(@)username] [value/all]"<br />

Examples: 	<br />
"!give @zmotan 69"<br />
"!give zmotan 420"<br />
"!give @zmotan all"<br />
"!give zmotan ALL"<br />

Note: Works with Youtube Tag or just with name ( "@zmotan" / "zmotan" )<br />
 ![Preview Image](https://github.com/zmotan/Streamlabs-Chatbot-Give-command-for-Youtube/blob/main/Preview.png)
 <br />

Possible parameters:<br />
$cost = points you want to give<br />
$user = giver name<br />
$points = how many points giver currently have<br />
$currency = currency name (set in chatbot)<br />
$command = command name<br />
![Preview SLChatbot](https://github.com/zmotan/Streamlabs-Chatbot-Give-command-for-Youtube/blob/main/PreviewSLChatbot.png)<br/>



Patch Notes:<br />
Version 4.20.69: <br />
Overengineered Fix: Users can have multiple spaces next to each other<br />

Known issues:<br />
API/Youtube chat limits:<br />
If user's first letter is AT - "@" or SPACE (" ") you have to tag it or use another @ in front to detect the correct user. (Example: user=@ndrei -> usage="!give @@ndrei 69")<br />
If there are 2 users with exactly same name (case insensetive) the points will be added to the first detected user in the viewer list.<br />
Users whos name ends with space (" ") or have multiple spaces ("  ") next to each other can't receive points. Youtube will reformat message and remove spaces meaning that user can't be find in database.<br /><br />

 
