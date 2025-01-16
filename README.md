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