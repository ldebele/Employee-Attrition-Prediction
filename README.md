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
    |
    ├──  data
    |       └── raw    <- Raw datasets.
    |
    ├── models      <- saved models.
    │
    ├── notebooks   <- Jupyter notebooks.
    │
    ├── reports     <- Generated figures.
    │
    ├── scripts
    |       ├── main.py
    |       |
    |       ├── predict.py
    |       |
    |       ├── preprocess.py
    |       |
    |       └── utils.py 
    | 
    ├── Makefile
    │
    ├── README.md
    │
    └── setup.py
    
      

## Requirements
To run the web app locally, you will need the following.
- category-encoders
- dvc
- joblib
- matplotlib
- numpy
- pandas 
- path
- pickleshare
- scikit-learn
- scipy
- seaborn
- statsmodels
- xbboost

## Getting Started
### Installation
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

## Author
- `Lemi Debele`