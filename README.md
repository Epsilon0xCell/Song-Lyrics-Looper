![Intro scenery: the pinned brass cylinder close up, its seam and cross mark showing at the left end, the steel comb teeth alongside it and crimson velvet lining the box](intro-banner.png)


# Song-Lyrics-Looper

![Wordmark banner: an open music box on crimson velvet, its pinned brass cylinder under the steel comb and the crank at the front](banner.png)

<p align="center"><img src="logo.png" alt="Song-Lyrics-Looper logo: a brass music box cylinder in macro seen through a round vignette, rows of tiny raised pins across its surface and one steel comb tooth resting on the pin about to play" width="200"></p>

![Animated scene](scene.svg)


> **Small board nailed below the main one:** with no arguments the song prints and the exit is 0; --help and -h print the usage note and exit 0; any other argument prints the usage note to standard error and exits 2; and the output never changes between runs.



# Song-Lyrics-Looper

A small Python script that prints the counting lyrics of the three times
table song: a counting-up chorus, the multiplication verses from 3 times
10 down to 3 times 1, then the chorus again.

Requirements: Python 3, standard library only. The script reads no
input.


![Separator](sep-heavy.svg)

## Run

```bash
python3 songlyricslooper.py
```

With no arguments it prints the song and exits 0. `--help` (or `-h`)
prints a one line usage note and exits 0. Any other argument prints
the usage note to stderr and exits 2, with none of the song printed.
I added the argument handling when I moved the song under a main
guard; before that, every argument was silently ignored and the song
printed anyway.


![Separator](sep-light.svg)

## What it prints

- The chorus line `3 6 9 12 15 18 21 24 27 30` twice.
- One verse per line for `3 times 10 is 30` down to `3 times 2 is 6`,
  followed by the closing line `3 times 1 is 3 of course`.
- The chorus line twice more, for four chorus lines in total.

The output is fixed: every run prints the same 41 lines. All ten
multiplication facts in the verses were checked against the 3 times
table and are correct. The restructure that added the main guard did
not change a single byte of the output; I checked the new output
against the old one with cmp before calling it done.


![Separator](sep-heavy.svg)

## Tests

```bash
python3 -m unittest
```

10 tests, all passing. They pin the full song text byte for byte,
the 41 line count, the four chorus lines, the verse products in
order, the closing line, and the argument behavior above, including
that importing the module prints nothing.


![Separator](sep-light.svg)

## Files

- `songlyricslooper.py` - the script
- `test_songlyricslooper.py` - the unittest suite
- `LICENSE` - GPL-3.0 license
- `logo.png`, `banner.png` - project branding
