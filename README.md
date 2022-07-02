# sena-analytics

# Main tools:

Python - Pandas - MongoDB - Decouple - Flask (For the Docker)

# How to Run?

1. Install python

2. Install pip lib to install dependencies using: `python3 -m pip install --user --upgrade pip`

3. Install virtual env using: `python3 -m pip install --user virtualenv`

4. Create a virtualenv for the project: `python3 -m venv env`

5. To activate it use: `source env/bin/activate`

6. Install the Python imports using `pip install -r requirements.txt`

7. Run the code files to activate the pipelines, example : `python tradedVolume.py`, having the env activated within the libs of last step


** `createIndexes.py` is for creating the indexes and constraints, this file needs to be run once.
** If having problems upolading data to mongodb, try running `python sslLoad.py` before pipeline file.

# How to Run on Docker?

1. `docker build -t python-flask:latest .`

2. `docker run -d python-flask`
