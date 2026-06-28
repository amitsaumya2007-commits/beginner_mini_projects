# Python Learning Workspace

This directory contains small, independent Python practice scripts and learning exercises used to explore Python fundamentals and small projects.

## Current files

- bottles.py — prints the "99 bottles of beer" lyrics using a generator.
- g_problems.py — assorted examples: generators, chunking, sliding windows, paragraph splitting, and small helpers.
- vowel_counter.py — interactive vowel counter (uses input()).
- num_guess.py — interactive number-guessing game with difficulty levels.
- experiments.py — example age calculator demonstration.
- magic_8_ball.py — interactive Magic 8-Ball toy.
- mean_median_mode.py — utility functions for mean, median, and mode with example usage.
- menu_calculator.py — simple ordering/total calculator (interactive).
- rck_ppr_scr.py — rock-paper-scissors game (interactive).
- requirements.txt — optional third-party dependencies (if any).

## Notes

- Most files contain top-level, interactive code and are intended to be run as scripts: `python3 <filename>.py`.
- When converting files into importable modules, move interactive sections under `if __name__ == "__main__":` to avoid running on import.
- A local virtual environment (`venv/`) may exist locally and is not tracked in source.

## How to use

1. (Optional) Activate the virtual environment:
   source venv/bin/activate
2. Run a script:
   python3 bottles.py


