# Introduction 
This project creates all boilerplate files / folders for development of a new model.

```
└───small_business_model
    ├───a_business_understanding
    ├───b_data_understanding
    ├───c_data_prep
    ├───d_modeling
    ├───e_evaluation
    ├───f_deployment
    │       small_business_model.py
    |       main.py
    └───g_communication
```

## Naming
All file / folder names should be lowercase, and should not include spaces. The cookiecutter template will automatically 'slugify' any names entered.

Python Class names follow [PEP 8](https://www.python.org/dev/peps/pep-0008/#id41) convention.

# Getting Started

## Install dependancies
Spawn new venv, and install requirements

```
python -m venv venv
./venv/scripts/activate.ps1
pip install -r requirements.txt
```

For Linux, use: `.\venv\bin\activate`

## Generate new model project
Use the following command to generate a new model:

`cookiecutter https://westfieldgrp.visualstudio.com/Data%20Science/_git/dsTemplates`

This will kick off a short series of prompts that the user will answer. Once complete, the user will have a directory with their model name, and all required sub-dirs. There will also be a boilerplate python file with the specified model class already added.

