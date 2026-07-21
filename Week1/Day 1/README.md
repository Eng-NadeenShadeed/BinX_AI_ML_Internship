## Day 1 - Environment Setup & the Jupyter Workflow

### Overview

Set up a professional, reproducible Python environment and learned the Jupyter Notebook workflow, along with basic Git version control.

### Files

- `day1_environment_setup.ipynb` - environment verification notebook

### Topics Covered

- Why a reproducible environment matters for AI/ML work
- Virtual environments (`venv`), `pip`, and `requirements.txt`
- The Jupyter Notebook workflow: code cells vs. Markdown cells
- Supporting tools: VS Code, Git & GitHub

### What Was Done

- Created and activated a Python virtual environment (`.venv`)
- Installed NumPy, Pandas, Matplotlib, Jupyter, and `ipykernel` inside the environment
- Built a notebook that imports each library and prints its version to confirm the setup
- Fixed a kernel issue where VS Code was not linked to the project's virtual environment (was defaulting to the global Python install) by installing `ipykernel` inside `.venv` and reloading VS Code
- Froze the environment to `requirements.txt` for reproducibility
- Initialized a Git repository and pushed the first commit to GitHub