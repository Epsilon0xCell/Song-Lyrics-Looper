# -*- coding: utf-8 -*-
"""
I wrote this in November 2023 to print the three times table as a song:
the counting chorus twice, the verses counting down, the closing line,
then the chorus twice more. It takes no arguments and reads no input,
so every run prints the same 41 lines and exits 0.
"""

# I use two separate repeat counters, one per chorus block. The closing
# block needs its own because repeat1 is already at 2 by then, so a
# shared counter would skip the final chorus entirely.

repeat1 = 0
repeat2 = 0

# I build the chorus once as a range and reuse it in both chorus
# blocks. A range can be walked more than once, unlike a generator, so
# the second block prints the same ten numbers without a rebuild.
countup = range(3, 31, 3)

# Two passes give exactly two chorus lines before the verses start.
# The end=" " keeps one chorus on one line; the numbers come out with
# a trailing space before the newline, which I leave as is because
# the line reads the same either way.
while repeat1 < 2:
    for x in countup:
        print(x,end=" ")
    print("\n")
    repeat1 = repeat1+1

# The verses count down, 10 first, because that is how the song goes.
# A range stops before its end value, so this one gives 10 down to 2
# and never reaches 1. That gap is why the 3 times 1 line is printed
# on its own after the loop. If I ever extend this range to include
# 1, that separate line has to go or the song would say it twice.
countdown = range(10, 1, -1)


# Each verse string starts with two newlines and a space, which is
# what puts the blank spacing between verses in the printed output.
for y in countdown:
 mult = 3*y
 print("\n \n 3 times" + " " + str(y) + " is" + " " + str(mult))             
# The closing line is a fixed string, not part of the loop, for the
# range reason above. Its wording differs on purpose: "of course" is
# the song's last word on the table, not a verse like the others.
print("\n \n 3 times 1 is 3 of course \n")
print("\n")

# Closing chorus. This block checks repeat2, not repeat1: repeat1 is
# spent, so testing it here would print nothing after the verses.

while repeat2 < 2:
    for x in countup:
        print(x,end=" ")
    print("\n")
    repeat2 = repeat2+1

