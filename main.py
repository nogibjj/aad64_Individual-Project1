import pandas as pd
from lib import average, med, standard_deviation, visualize_data

df = pd.read_csv("RiskData_SumScores.csv")

print("Mean Risk Preferences of the sample is: " + str(average(df.loc[:, "Happy"])))

print("Median Risk Preferences of the given sample is: " + str(med(df.loc[:, "Happy"])))

print(
    "Standard Deviation Risk Preferences is: "
    + str(standard_deviation(df.loc[:, "Happy"]))
)


def summary_stats(data):
    result = data.describe()
    return result
