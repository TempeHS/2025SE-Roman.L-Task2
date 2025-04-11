[![Python Version](https://img.shields.io/badge/python-3.12.2-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3122/)

# Seoul Bike Sharing Demand Predictor

### Diagrams

[.working_documents](.working_documents)

## 1. MLOps Design Phase

### 1.1 Business Problem

**Domain knowledge:** Urban mobility and transportation

- Places where rental bikes are used may be redundent due to weather conditions and can waste resources which would be beneficial elsewhere.

- To address this, the Seoul Metropolitan Government has commisioned me to develop a machine-learning model which predicts rental frequency.

### 1.2 Refactoring the business problem

- A machine-learning model which predicts the amount of bikes required over weather and time conditions.

### 1.3 Defining success metrics

- Model generalises well to training data
- Model generalises well to testing data

### 1.4 Available data

I sourced a validated raw data set (https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand). The data is saved in the CSV file [2.1.2.SeoulBikeData_Sample_Data.csv.](2.model_development/2.1.data_wrangling/2.1.2.SeoulBikeData_Sample_Data.csv)

The data columns are:

| Column         | Description                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------- |
| date           | The date of the observation, used to track daily trends and seasonal patterns.                  |
| count          | The number of bikes rented during the specified hour, which is the target variable to predict.  |
| hour           | The hour of the day, used to capture time-based trends such as rush hours.                      |
| temp           | The temperature in Celsius, a key factor influencing bike-sharing demand.                       |
| humidity       | The percentage of humidity, which affects user comfort and bike usage.                          |
| windspeed      | The wind speed in meters per second, which can impact the ease of biking.                       |
| visibility     | The visibility in meters, which affects safety and user behavior.                               |
| dewpointemp    | The dew point temperature in Celsius, indicating moisture in the air and its effect on comfort. |
| solarradiation | The amount of solar radiation in MJ/m², which influences weather conditions and bike demand.    |
| rainfall       | The amount of rainfall in mm, which can deter bike usage.                                       |
| snowfall       | The amount of snowfall in cm, which can significantly reduce bike-sharing demand.               |
| seasons        | The season of the year (Spring, Summer, Fall, Winter), capturing seasonal variations in demand. |
| holiday        | To account for changes in demand on holidays.                                                   |
| functionday    | To exclude non-operational days.                                                                |

[Engineered Features](/workspaces/2025SE-Roman.Lac-Task2/2.model_development/2.1.data_wrangling/2.1.2.data.records.md)

## Getting Started

### Dependencies

- Windows 11

```
numpy
matplotlib
pandas
scikit-learn
keras
tensorflow
pydot
graphviz
pydot-ng
pillow
pydotplus
```

```
Flask
flask-wtf
flask-csp
flask-limiter
python-dotenv
```

### Installing

- Clone GitHub repository

```
https://github.com/TempeHS/2025SE-Roman.L-Task2
```

### Executing program

- Install requirements

```
pip install -r requirements.txt
```

- Model development is split into 4 sections, each with interactable and documented Jupyter notebooks:
  - [2.1.data_wrangling](2.model_development/2.1.data_wrangling)
  - [2.2.feature_engineering](2.model_development/2.2.feature_engineering)
  - [2.3.model_training](2.model_development/2.3.model_training)
  - [2.4.model_testing_and_Evaluation](2.model_development/2.4.model_testing_and_validation)

#### To run deploy Seoul Bike Demand Predictor UI

- Change directory

```
cd 3.operations/3.1.deploy_model
```

- Run system

```
python main.py
```

Once deployed, the UI can be accessed on either:

    http://localhost:5000
    http://127.0.0.1:5000

## Authors

Contributors names and contact info:

Roman Lacbungan -
[@RomanLac](https://github.com/RomanLac)

## Version History

- 0.6
  - Deployed model
- 0.5
  - Completed model evaluation
  - Started UI
- 0.4
  - Completed testing linear/polynominal regression
- 0.3
  - Completed feature engineering
- 0.2
  - Completed data wrangling
  - See [commit change](https://github.com/TempeHS/2025SE-Roman.L-Task2/commit/ecf67dcf44eb707d21ad7196962b72cec9d78bda)
- 0.1
  - Initial Release

* I did not use branches however this would have allowed new features being implemented while keeping the main branch unaffected

## License

This project is licensed under the GNU License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.

- [Github md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [TempeHS Jupyter-Notebook template](https://github.com/TempeHS/TempeHS_Jupyter-Notebook_DevContainer)
- [TempeHS MLOps template](https://github.com/TempeHS/MLOps)
- [Roman.L 2025 Developer Log](https://github.com/TempeHS/2025SE-Roman.L-HSCTask1)
