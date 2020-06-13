# RoboMod
A (hopefully working) Python discord moderation bot.


# Setup
To make your bot work, make sure you have the bot user on Discord Developer Portal ready.

Requirements:
Visual Studio Code
Basic Python knowledge
Python 3.8 or newer

Open up `main.py` in Visual Studio Code.
Find this code:

`TOKEN = 'your token'`
`clientid = 'your client ID'`

Paste your bots token in TOKEN, and the client ID in clientid.
Next, open up a terminal in your bots directory. RUn the following command:

Windows:
`py -3 -m pip install -U discord.py`
Linux and macOS:
`python3 -m pip install -U discord.py`

Now it is time to run your bot. Run this command:

Windows: 
`python main.py`
Linux and macOS:
`python3 main.py`


# Inviting your bot

A bot is useless if you can't use it. So to invite it to a server, open up the OAuth2 tab in Discord Developer Portal.
Next, check the `Bot` scope, and scroll down and select Administrator. Then copy the invite link ad invite it to your server. Enjoy!

