# Raspberry Pi Python Workshop

## Task

Clone this project onto your Raspberry Pi and work from the terminal. Set up a virtual environment, then fix the TODOs and the minimum and maximum calculations in `main.py`. Verify the results, commit your fix, and push it to a new repository on your GitHub account.

## Expected output

The program displays a table with these results:

```text
Number of Readings  8
Average             71.00 °F
Minimum             66.80 °F
Maximum             75.10 °F
Classification      comfortable
```

## Temperature classification

Classify the average temperature in °F:

- **Cool:** below 68 °F.
- **Comfortable:** 68 °F through 73 °F, inclusive.
- **Warm:** above 73 °F.

## Helpful commands

```sh
python3 -m venv .venv             # Create a virtual environment
source .venv/bin/activate         # Activate it
python -m pip install -r requirements.txt  # Install dependencies

cat -n main.py                    # Read the code with line numbers
grep -n TODO main.py              # Find the tasks to complete
python main.py                    # Run the analyzer
python -m py_compile main.py      # Check for syntax errors
git diff                          # Review your code changes
git status                        # See which files changed
git add main.py                   # Stage the corrected program
git commit -m "Fix temperature analyzer"  # Save the fix in Git
git remote rename origin upstream # Keep the instructor repository as upstream
git remote add origin https://github.com/USERNAME/REPO.git  # Add your new repository
git push -u origin main           # Upload your commit
```
