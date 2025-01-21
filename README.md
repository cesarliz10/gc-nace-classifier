# GC NACE Classifier

Service to classify commodities under a NACE econimic activity and extract the likely raw materials.




## Installation

The following instructions have been tested on a UNIX (Mac) system within an Iterm terminal. 
The only assumption is that a python >3.7 version is available: 

1. **Pre-requisites**:
 Install and configure pyenv (for python version mgmt) and poetry: 

- Install poetry: ``pip install poetry``
- Install pyenv:``brew install pyenv``
- Add pyenv root directory to `PATH`:
  ```bash 
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc 
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  ```
- Run updated `.zshrc` config: `source ~/.zshrc` 
2. Clone this repository:
```bash
git clone git@github.com:cesarliz10/gc-nace-classifier.git
```
3. Configure python local version:
```bash
cd gc-nace-classifier
pyenv install 3.10.15
pyenv local 3.10.15
```
4. Configure poetry to use local python for virtual env:
```bash
poetry env use $(pyenv which python)
```
5. Activate virtual environment and install package
```bash
poetry shell
poetry install
```

## Usage instructions

Within an activated (poetry) environment, follow these steps:

1. Launch the application:
```bash
uvicorn gc_nace_classifier.main:app
```
- Take the URL where the application is running. It should be printed in a message like: 
`INFO:     Uvicorn running on http://127.0.0.1:8000`


2. NACE Classification: 
- On a different terminal session, make a request to the `classify-nace` endpoint of the app. Ex: (curl):
```bash
curl -X POST "http://127.0.0.1:8000/classify-nace" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@<absolute-project-path>/gc-nace-classifier/data/<input-file>.csv"
```
- `<absolute-project-path>` is the placeholder for the absolute path to the repo.
- `<input-file>` is the placeholder for the name of the input csv to be used (ex: anonymized_data_300.csv).


3. Raw material extraction: 
- On a different terminal session, make a request to the `infer-raw-materials` endpoint of the app. Ex: (curl):
```bash
curl -X POST "http://127.0.0.1:8000/infer-raw-materials" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@<absolute-project-path>/gc-nace-classifier/data/<input-file>.csv"
```

## Project structure

```
gc-nace-classifier/
│
├── gc_nace_classifier/
│   ├── __init__.py
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # Pydantic models
│   ├── preprocess.py         # Data preprocessing
│   ├── classify.py           # NACE Classification
│   ├── inference_materials.py   # Raw material extraction
│
├── tests/  # ToDo
│
├── .python-version
├── poetry.lock
├── pyproject.toml
├── README.md                 # Documentation
└── data/                     # Sample .csv data

```