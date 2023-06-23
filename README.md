# Employee-Attrition-Prediction

## Table of contents
- Overview
- Datasets
- Project Structure
- Requirements
- Getting Started
- Author

## Overview
The aim of this project is to provide accurate predictions of employee attrition within an organization by analyzing multiple employee-related features.

## Datasets
This data set created by IBM data scientists.
- [Link to download the dataset](https://zenodo.org/record/4088439#.Y9Y3rtJBwUE)

## Project Structure 

    ├──  data
    |       └── raw    <- Raw datasets.
    ├── models         <- saved models.
    │
    ├── notebooks      <- Jupyter notebooks.
    │
    ├── reports        <- Generated figures.
    │
    ├── scripts
    |       ├── main.py
    |       ├── predict.py
    |       ├── preprocess.py
    |       └── utils.py 
    | 
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    └── setup.py
    
      

## Requirements
To run the web app locally, you will need the following.
- dvc
- matplotlib
- pandas 
- scikit-learn
- streamlit
- xgboost

## Getting Started
### Installation
#### Setup the Environment
- create a virtualenv with Python 3.7 and activate it.
```
python3 -m vevn venv
source venv/bin/activate
```
#### 2. Clone the repository.
```
git clone https://github.com/ldebele/Employee-Attrition-Prediction
cd Employee-Attrition-Prediction 
make install
```
### Run
To run the web locally
```
make run
``` 

### Web App 
This app is Employee Attrition Prediction. It predict whether the employee is Stay or Leave the company based on some features.

Deployment is done on streamlit.io - [web App](https://ldebele-employee-attrition-prediction-scriptsmain-ry3t4v.streamlit.app/)
## Author
- `Lemi Debele`