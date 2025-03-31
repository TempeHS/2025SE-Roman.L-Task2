# Seoul Bike Sharing Demand

Source dataset: https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand

Domain knowledge: Urban mobility and transportation

Predicts the amount of bikes required over conditions.

## Description

An in-depth paragraph about your project and overview of use.

Students are to assume the role of data scientists or engineers and follow an MLOps process to engineer a machine-learning model for an emerging audience. Students are encouraged to identify their own data set and ‘business problem’ based on their interests.

## Business Problem

Places where rental bikes are used may be redundent due to weather conditions and can waste resources which would be beneficial elsewhere. To address this, the Seoul Metropolitan Government has commisioned me to develop a machine-learning model which predicts rental frequency based on weather conditions.

## Features

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

### Installing

- How/where to download your program
- Any modifications needed to be made to files/folders

### Executing program

- How to run the program
- Step-by-step bullets

```
code blocks for commands
```

## Help

Any advise for common problems or issues.

```
command to run if program contains helper info
```

## Authors

Contributors names and contact info:

Roman Lacbungan -
[@RomanLac](https://github.com/RomanLac)

## Version History

- 0.2
  - Various bug fixes and optimizations
  - See [commit change]() or See [release history]() or see [branch]()
- 0.1
  - Initial Release

## License

This project is licensed under the GNU License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.

- [Github md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [TempeHS Jupyter-Notebook template](https://github.com/TempeHS/TempeHS_Jupyter-Notebook_DevContainer)
- [TempeHS MLOps template](https://github.com/TempeHS/MLOps)
