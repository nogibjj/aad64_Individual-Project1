from lib import average, med, standard_deviation, visualize_data

import pandas as pd

testing_data = pd.read_csv("RiskData_SumScores.csv")


def testing_main_avg():
    assert average(testing_data.loc[:, "Happy"]) == 75.29


def testing_main_med():
    assert med(testing_data.loc[:, "Happy"]) == 78.5


def testing_main_std():
    assert standard_deviation(testing_data.loc[:, "Happy"]) == 14.41


testing_main_avg()
testing_main_med()
testing_main_std()

# Testing Usage of Visualization function:

visualize_data(
    testing_data,
    "SES",
    "RiskPreferences",
    hue="Gender",
    title="Violin Plot for Age vs Risk Preferences,"
    + "\n"
    + "separated by Gender [1: Male; 2: Female]",
    xlabel="Socioeconomic Status",
    ylabel="Risk Preferences",
)
