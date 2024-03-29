# sena-analytics

# Main Python libs:

Pandas - MongoDB - Decouple - Flask (For the Docker)

# How to Run?

1. Install python

2. Install pip lib to install dependencies using: `python3 -m pip install --user --upgrade pip`

3. Install virtual env using: `python3 -m pip install --user virtualenv`

4. Create a virtualenv for the project: `python3 -m venv env`

5. To activate it use: `source env/bin/activate`

6. Install the Python imports using `pip install -r requirements.txt`

7. Set code variables on a `.env` file as `.env.example` shows

8. Run `createIndexes.py` for creating the indexes and constraints, this file needs to be run only once.

9. Run the code files to activate the pipelines, example : `python tradedVolume.py`, having the env activated within the libs of last step
  - List of python pipelines files: `tradedVolume.py`, `dailyTradedVolumeSENA.py`, `floorPriceSENA.py`, `NFTTradedVolume.py`, `senaNFTRoyalties.py`, `totalTransactions.py`, `tradedVolumeSENA.py`



** If having problems upolading data to mongodb, try running `python sslLoad.py` before pipeline file.

** Pipelines are online and scheduled to run daily on heroku.com, so the docker build is only for demonstration

** Pipelines connected to devnet sometimes return no data, the code will print where no data stops the pipeline process and finish running normally

# How to Run on Docker?

1. `docker build -t sena-analytics:latest .`

2. `docker run -d sena-analytics`
