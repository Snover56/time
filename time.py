# Written by Matthew Quinn
# Last updated: 6/9/20

import random
import time

numbercorrect = 0
input('This game is called time.\n>>> ')
print('You have 2 seconds to press enter the number of times it says on the screen.')
print('Once you think time is up, press enter one more time to progress onto the next question.')
input('Press enter to begin.\n>>> ')

while(True):
    times = random.randint(0,12)
    starttime = time.monotonic()
    inputs = 0
    currenttime = time.monotonic()
    print('\n' + str(times))
    while(currenttime - starttime <= 2.0):
        if inputs == 0:
            input('>>> ')
        else:
            input(inputs)
        inputs += 1
        currenttime = time.monotonic()
    if inputs == times + 1:
        numbercorrect += 1
    else:
        print('Game over!')
        time.sleep(1)
        print('Your answered ' + str(numbercorrect) + ' correctly.')
        input('Press enter to try again\n>>> ')
