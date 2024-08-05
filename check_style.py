#!/usr/bin/python3
"""
A script to check for pycodestyle compliance in the project files.
"""

import subprocess
import sys

def run_pycodestyle():
    """Run pycodestyle on all Python files in the current directory."""
    try:
        result = subprocess.run(
            ["pycodestyle", "."],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("All files are pycodestyle compliant!")
        else:
            print("Pycodestyle issues found:")
            print(result.stdout)
            sys.exit(result.returncode)
    except FileNotFoundError:
        print("pycodestyle is not installed. Please install it to run this script.")
        sys.exit(1)

if __name__ == "__main__":
    run_pycodestyle()
