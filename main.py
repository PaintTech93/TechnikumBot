'''This Voice Assistant was built for a university project
   Major thanks goes to the following sites, as to information
   regarding how to build an own Voice-based assistant
   https://dev.to/coderasha/build-virtual-assistant-with-python-automate-tasks-46a6
   https://pythonspot.com/personal-assistant-jarvis-in-python/
   https://towardsdatascience.com/build-your-first-voice-assistant-85a5a49f6cc1'''

from technikumbot import technikumbot
from speak import myCommand
from talk import talk



talk('Technikum Bot is ready!')
#loop to continue executing multiple commands


while True:
    technikumbot(myCommand())
