Name: Give Points
Version: 4.20.69
Creator: zmotan
Website: https://zmotan.com

4.20.69 Overengineered Patch Notes:
Fix: Users can have multiple spaces next to each other

API limits:
If user's first letter is @ you have to tag it or use another @ infront to detect the correct user. (Example: user= @ndrei -> usage= "!give @@ndrei 69")
If there are 2 users with exactly same name (case insensetive) the points will be added to the first detected user in the viewer list.


Note: Works with Youtube Tag or just with name ( "@zmotan" / "zmotan" )
Preview Image - https://github.com/zmotan/Streamlabs-Chatbot-Give-command-for-Youtube/blob/main/Preview.png

Template:
"[command] [(@)username] [value/all]"

Examples:
"!give @zmotan 69"
"!give zmotan 420"
"!give @zmotan all"
"!give zmotan ALL"

Possible parameters:
$cost = points you want to give
$user = giver name
$points = how many points giver currently have
$currency = currency name (set in chatbot)
$command = command name
Preview SLChatbot - https://github.com/zmotan/Streamlabs-Chatbot-Give-command-for-Youtube/blob/main/PreviewSLChatbot.png