# optimal_retrocession
codes and notebook about optimal reinsurance retrocession

## Project Structure

*   `memoire/`: Contains the LaTeX source files for the dissertation.
*   `scripts/`: Contains the Python scripts used for analysis and generating results.
*   `results/`: Contains the outputs of the scripts (plots, data files, etc.). This directory is ignored by Git.
*   `contexte.md`: Contains the project context and objectives.

## Getting Started

This project uses `uv` for dependency management and `direnv` to automatically activate the virtual environment.

1.  **Allow `direnv` to run:**

    The first time you enter this directory, you will need to allow `direnv` to load the environment:

    ```bash
    direnv allow
    ```

2.  **Install dependencies:**

    The virtual environment is now active. You can install the dependencies with `uv`:

    ```bash
    uv pip install -r requirements.txt
    ```