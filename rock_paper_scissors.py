#!/usr/bin/env python3
import numpy as np
import random
import sys
from time import sleep

try:
    import sounddevice as sd
except ImportError:
    sd = None

P = {"r": "rock", "p": "paper", "s": "scissors"}
FS = 44100  # needs to be int, non-44100 may not work on HDMI


def main():
    print_choices()

    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    else:
        N = 10

    stat = 0
    wins = 0
    losses = 0

    for _ in range(N):
        computer = random.choice(list(P.keys()))

        try:
            human = input()
            if human not in P.keys():
                print_choices()
                continue
        except EOFError:
            print("goodbye")
            break

        if human == computer:
            print("draw!")
            stat = 0
        elif human == "r":
            if computer == "s":
                print("Human win: ⭖ smashes ✄")
                stat = 1
            else:
                print("computer wins: 📰 covers ⭖")
                stat = -1
        elif human == "s":
            if computer == "r":
                print("computer wins: ⭖ smashes ✄")
                stat = -1
            else:
                print("human wins: ✄ cuts 📰")
                stat = 1
        elif human == "p":
            if computer == "s":
                print("computer wins: ✄ cuts 📰")
                stat = -1
            else:
                print("human wins: 📰 covers ⭖")
                stat = 1

        if stat == 1:
            wins += 1
        elif stat == -1:
            losses += 1

        feedback(stat)

    print("Wins:", wins, "losses:", losses)


def print_choices():
    for k, v in P.items():
        print(k, v, end="  ")


def feedback(stat: int):
    global sd

    if sd is None:
        return

    if stat == -1:
        f1 = 700.0
        f2 = 400.0
    elif stat == 1:
        f1 = 400.0
        f2 = 700.0
    else:
        return

    T = 0.3
    tp = 0.2

    t = np.arange(0, T + tp, 1 / FS)
    Nt = t.size
    Np = int(tp // FS)
    ih = (Nt - Np) // 2

    sound = np.empty_like(t)
    sound[Np:ih] = np.sin(2 * np.pi * f1 * t[Np:ih])
    sound[ih:] = np.sin(2 * np.pi * f2 * t[ih:])

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
        ax.set_xlabel("time [sec]")

        show()


if __name__ == "__main__":
    main()
