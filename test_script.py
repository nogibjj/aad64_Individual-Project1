import pandas as pd
from main import summary_stats

df = pd.read_csv("RiskData_SumScores.csv")

print(
    "Overall summary statistics of full dataset relating to Risk Data is: "
    + "\n"
    + str(summary_stats(df))
)
