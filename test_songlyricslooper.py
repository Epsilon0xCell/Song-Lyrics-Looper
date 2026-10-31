"""Tests for songlyricslooper.py.

The song text is fixed, so most of these pin the exact output: the
chorus wording, the verse products, the blank line layout, and the
41 line total. The rest pin the argument behavior I added with the
main guard: --help exits 0, anything else exits 2, and importing the
module prints nothing.
"""
import contextlib
import io
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).parent
SCRIPT = HERE / "songlyricslooper.py"
sys.path.insert(0, str(HERE))

import songlyricslooper  # noqa: E402

CHORUS_LINE = "3 6 9 12 15 18 21 24 27 30 "
CHORUS_BLOCK = (CHORUS_LINE + "\n\n") * 2
VERSES = "".join(
    f"\n \n 3 times {y} is {3 * y}\n" for y in range(10, 1, -1)
)
CLOSING = "\n \n 3 times 1 is 3 of course \n\n" + "\n\n"
EXPECTED = CHORUS_BLOCK + VERSES + CLOSING + CHORUS_BLOCK


def run_main(argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = songlyricslooper.main(argv)
    return code, out.getvalue()


def run_script(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True, text=True, timeout=30,
    )


class OutputTests(unittest.TestCase):
    def test_full_output_matches_expected_text(self):
        code, out = run_main([])
        self.assertEqual(code, 0)
        self.assertEqual(out, EXPECTED)

    def test_output_is_41_lines(self):
        _, out = run_main([])
        self.assertEqual(len(out.splitlines()), 41)

    def test_chorus_line_printed_four_times(self):
        _, out = run_main([])
        lines = [line.rstrip() for line in out.splitlines()]
        self.assertEqual(lines.count(CHORUS_LINE.rstrip()), 4)

    def test_verses_have_correct_products_in_order(self):
        _, out = run_main([])
        positions = []
        for y in range(10, 1, -1):
            needle = f"3 times {y} is {3 * y}"
            self.assertIn(needle, out)
            positions.append(out.index(needle))
        self.assertEqual(positions, sorted(positions))

    def test_closing_line_printed_once(self):
        _, out = run_main([])
        self.assertEqual(out.count("3 times 1 is 3 of course"), 1)


class ArgumentTests(unittest.TestCase):
    def test_script_no_args_exits_0(self):
        result = run_script()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, EXPECTED)

    def test_help_exits_0_without_the_song(self):
        result = run_script("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("usage", result.stdout)
        self.assertNotIn("3 times 10", result.stdout)

    def test_short_help_exits_0(self):
        code, out = run_main(["-h"])
        self.assertEqual(code, 0)
        self.assertIn("usage", out)

    def test_unknown_argument_exits_2_and_prints_no_song(self):
        result = run_script("verse")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("usage", result.stderr)

    def test_import_prints_nothing(self):
        result = subprocess.run(
            [sys.executable, "-c", "import songlyricslooper"],
            capture_output=True, text=True, timeout=30, cwd=HERE,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
