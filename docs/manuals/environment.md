# Environment

For consistency across all pc-s we need to keep track of dependencies and required libraries. We will be using a virtual environment to manage these dependencies called Poetry. Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

## Installation

On macOS and Linux, you can install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

On Windows, you can install Poetry via PowerShell

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Usage
To innitialize a new project with Poetry, run the following command in your terminal

```bash
poetry new my_project
```

or to init poetry in an existing project

```bash
poetry init
```

To add a new dependency to your project, run the following command in your terminal

```bash
poetry add package_name
```

To access the virtual environment created by Poetry, run the following command in your terminal

```bash
poetry shell
```

To install all dependencies in your project, run the following command in your terminal

```bash
poetry install --sync
```
