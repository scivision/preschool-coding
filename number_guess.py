#!/usr/bin/env python3
import random
import argparse
import sys

try:
    import num

    isprime = num.numerical.isprime
except ImportError as err:
    print(err)
    isprime = None


def get_guess(msg: str, imin: int, imax: int) -> int:
    try:
        guess = int(input(msg + "\n"))
    except ValueError:
        print("not a number, try again", file=sys.stderr)
        guess = get_guess(msg, imin, imax)

    if not imin <= guess <= imax:
        print(f"guess between {imin}..{imax}", file=sys.stderr)
        guess = get_guess(msg, imin, imax)

    return guess


def main(maxtry: int, imin: int, imax: int):

    secret = random.randint(imin, imax)

    if isprime is not None:
        pstr = "prime" if isprime(secret) else "non-prime"

    estr = "odd" if secret % 2 else "even"

    msg = f"guess my {pstr} {estr} number between {imin}..{imax} "

    for i in range(1, maxtry + 1):
        try:
            guess = get_guess(msg, imin, imax)
        except EOFError:
            print("goodbye")
            return

        if guess < secret:
            msg = f"it's bigger than {guess} "
        elif guess > secret:
            msg = f"it's smaller than {guess} "
        elif guess == secret:
            print(f"you guessed my secret {secret} in {i} turns -- hooray!")
            return
        else:
            raise ValueError("impossible")

    raise SystemExit(f"too many tries, sorry, game over--real answer was {secret}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-maxtry", help="maximum number of guesses", type=int, default=10)
    p.add_argument(
        "-minmax", help="minimum, maximum number to guess", type=int, nargs=2, default=[1, 100]
    )
    P = p.parse_args()

    main(P.maxtry, *P.minmax)
