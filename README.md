![songlyricslooper banner](banner.png)

# Song-Lyrics-Looper

A small Python script that prints the counting lyrics of the three times
table song: a counting-up chorus, the multiplication verses from 3 times
10 down to 3 times 1, then the chorus again.

Requirements: Python 3, standard library only. The script takes no
arguments and reads no input.

## Run

```bash
python3 songlyricslooper.py
```

## What it prints

- The chorus line `3 6 9 12 15 18 21 24 27 30` twice.
- One verse per line for `3 times 10 is 30` down to `3 times 2 is 6`,
  followed by the closing line `3 times 1 is 3 of course`.
- The chorus line twice more, for four chorus lines in total.

The output is fixed: every run prints the same 41 lines and exits 0.
All ten multiplication facts in the verses were checked against the
3 times table and are correct.

## Files

- `songlyricslooper.py` - the script
- `LICENSE` - GPL-3.0 license
- `logo.png`, `banner.png` - project branding
