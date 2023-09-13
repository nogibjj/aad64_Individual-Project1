import pandas as pd
import matplotlib.pyplot as plt

print("Mean of Sepal Lengths in iris.csv: " + 
      str(average(df.iloc[:, 1])))
print("Median of Sepal Lengths in iris.csv: " + 
      str(med(df.iloc[:, 1])))
print("Standard Deviation of Sepal Lengths in iris.csv: " + 
      str(standard_deviation(df.iloc[:, 1])))
print("Overall summary statistics of full dataset iris.csv: " + 
      "\n" + str(summary_stats(df)))