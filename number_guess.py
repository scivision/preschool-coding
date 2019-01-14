#!/usr/bin/env python
import random

secret = random.randint(1, 100)

msg = 'guess my number '

while True:
    try:
        guess = int(input(msg))
    except EOFError:
        print('goodbye')
        break

    if guess < secret:
        msg = 'try bigger '
    elif guess > secret:
        msg = 'try smaller '
    elif guess == secret:
        print('you guessed my secret number -- hooray!')
        break
    else:
        raise RuntimeError('impossible')
