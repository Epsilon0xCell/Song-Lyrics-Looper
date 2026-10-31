# -*- coding: utf-8 -*-
"""
I wrote this in November 2023 to print the three times table as a song:
the counting chorus twice, the verses counting down, the closing line,
then the chorus twice more. It reads no input. Run with no arguments
it prints the same 41 lines and exits 0; --help prints a short usage
line and exits 0, and any other argument exits 2 without printing
the song.
"""

import sys

USAGE = "usage: python3 songlyricslooper.py [--help]"

# I build the chorus once as a range and reuse it in both chorus
# blocks. A range can be walked more than once, unlike a generator, so
# the second block prints the same ten numbers without a rebuild.
countup = range(3, 31, 3)


def print_chorus():
    # Two passes give exactly two chorus lines. Each pass has its own
    # loop count, so the closing block does not need a second counter:
    # an earlier version kept repeat1 and repeat2 by hand because one
    # shared counter would have been spent by the closing block and
    # skipped the final chorus entirely.
    # The end=" " keeps one chorus on one line; the numbers come out
    # with a trailing space before the newline, which I leave as is
    # because the line reads the same either way.
    for _ in range(2):
        for x in countup:
            print(x, end=" ")
        print("\n")


def print_verses():
    # The verses count down, 10 first, because that is how the song
    # goes. A range stops before its end value, so this one gives 10
    # down to 2 and never reaches 1. That gap is why the 3 times 1
    # line is printed on its own after the loop. If I ever extend
    # this range to include 1, that separate line has to go or the
    # song would say it twice.
    countdown = range(10, 1, -1)
    # Each verse string starts with two newlines and a space, which
    # is what puts the blank spacing between verses in the printed
    # output.
    for y in countdown:
        mult = 3 * y
        print("\n \n 3 times" + " " + str(y) + " is" + " " + str(mult))
    # The closing line is a fixed string, not part of the loop, for
    # the range reason above. Its wording differs on purpose: "of
    # course" is the song's last word on the table, not a verse like
    # the others.
    print("\n \n 3 times 1 is 3 of course \n")
    print("\n")


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if args == ["--help"] or args == ["-h"]:
        print(USAGE)
        return 0
    if args:
        print(USAGE, file=sys.stderr)
        return 2
    print_chorus()
    print_verses()
    # Closing chorus. print_chorus counts its own two passes, so
    # calling it again here prints the full chorus instead of
    # nothing.
    print_chorus()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
