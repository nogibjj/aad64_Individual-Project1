import pandas as pd

from lib import average, med, standard_deviation, summary_stats, visualize_data

df = pd.read_csv("RiskData_SumScores.csv")

print("Mean Risk Preferences of the sample is: " + str(average(df.loc[:, "Happy"])))

print("Median Risk Preferences of the given sample is: " + str(med(df.loc[:, "Happy"])))

print(
    "Standard Deviation Risk Preferences is: "
    + str(standard_deviation(df.loc[:, "Happy"]))
)

print(
    "Overall summary statistics of full dataset relating to Risk Data is: "
    + "\n"
    + str(summary_stats(df))
)

visualize_data(
    df,
    "SES",
    "RiskPreferences",
    hue="Gender",
    title="Violin Plot for Age vs Risk Preferences,"
    + "\n"
    + "separated by Gender [1: Male; 2: Female]",
    xlabel="Socioeconomic Status",
    ylabel="Risk Preferences",
)
