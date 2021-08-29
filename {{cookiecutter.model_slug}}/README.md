# Installing Libraries:
Libraries, and their required versions, are listed in the requirements.txt or environment.yl file depending if base Python or Anaconda is being used.  To install them, run either the conda or pip commands listed below:

## Anaconda:
```
conda env create -f environment.yml
conda activate env_batch_{{cookiecutter.model_class}}
```

## PIP:
```
python -m env env_batch_{{cookiecutter.model_class}} 
.\env_batch_{{cookiecutter.model_class}}\Scripts\activate
pip install -r requirements.txt --target
```