from random import randint
import os
responses = [
    "As the prophecy foretold.",
    "But at what cost?",
    "So let it be written; so let it be done.",
    "That's just what he/she/they would've said",
    "Is this why fate brought us together?",
    "And thus, I die.",
    "...just like in my dream...",
    "Be that as it may, still may it be as it may be",
    "There is no escape from destiny",
    "Is this economy?",
    "...and then the wolves came.",
    "But everything changed when The Fire Nation Attacked"
]

chosenResponse = responses[randint(0,len(responses)-1)]
cmd = 'echo %s | pbcopy' % chosenResponse
os.system(cmd)
