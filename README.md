# Sentimental Analysis

## Installation (in Linux)
There are two ways to install the required dependenicies

Using requirements.txt
- First create a virtual environment and go into it using:
  [your_python_interpreter] -m venv [any_virtual_environment_name] ; source [any_virtual_environment_name/bin/activate]
example:
```
   python3.12 -m venv .env ; source .env/bin/activate
```
- Then install the dependenicies using:
  [your_python_interpreter] -m pip install -r requirements.txt

example:
```
    python3.12 -m pip install -r requirements.txt
```

Using poetry

- first install pipx from https://pipx.pypa.io/stable/installation/
  then  to install poetry use:

```
  pipx install poetry
```

- To install dependencies use:

```
  poetry install 
```

## Running the project
```
 ./run.sh
```

- Next check the graphs generated in visuals directory

