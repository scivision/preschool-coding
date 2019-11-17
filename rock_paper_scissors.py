#!/usr/bin/env python3
import numpy as np
import random
from time import sleep
try:
    import sounddevice as sd
except ImportError:
    sd = None

P = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
FS = 44100  # needs to be int, non-44100 may not work on HDMI


def main():
    print_choices()

    while True:
        computer = random.choice(list(P.keys()))

        try:
            human = input()
            if human not in P.keys():
                print_choices()
                continue
        except EOFError:
            print('goodbye')
            break

        if human == computer:
            print('draw!')
            stat = 0
        elif human == 'r':
            if computer == 's':
                print('Human win: rock smashes scissors')
                stat = 1
            else:
                print('computer wins: paper covers rock')
                stat = -1
        elif human == 's':
            if computer == 'r':
                print('computer wins: rock smashes scissors')
                stat = -1
            else:
                print('human wins: scissors cuts paper')
                stat = 1
        elif human == 'p':
            if computer == 's':
                print('computer wins: scissors cuts paper')
                stat = -1
            else:
                print('human wins: paper covers rock')
                stat = 1

        feedback(stat)


def print_choices():
    for k, v in P.items():
        print(k, v, end='  ')


def feedback(stat: int):
    global sd

    if sd is None:
        return

    if stat == -1:
        f1 = 700.
        f2 = 400.
    elif stat == 1:
        f1 = 400.
        f2 = 700.
    else:
        return

    T = 0.3
    tp = 0.2

    t = np.arange(0, T+tp, 1/FS)
    Nt = t.size
    Np = int(tp//FS)
    ih = (Nt-Np)//2

    sound = np.empty_like(t)
    sound[Np:ih] = np.sin(2*np.pi*f1*t[Np:ih])
    sound[ih:] = np.sin(2*np.pi*f2*t[ih:])

    try:
        sd.play(sound, FS)
    except Exception as err:
        sd = None
        print(f"Error with sound playback, disabling.  Error: {err}")

    sleep(T)

    if False:
        from matplotlib.pyplot import figure, show
        ax = figure().gca()
        ax.plot(t, sound)
        ax.set_xlabel('time [sec]')

        show()


if __name__ == '__main__':
    main()
