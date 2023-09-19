from lib import average, med, standard_deviation, summary_stats, visualize_data
import pandas as pd

df = pd.read_csv("RiskData_SumScores.csv")


def testing_main_avg_input():
    assert average(None) == "Please provide valid DataFrame type input."


def testing_main_med_input():
    assert med(None) == "Please provide valid DataFrame type input."


def testing_main_std_input():
    assert standard_deviation(None) == "Please provide valid DataFrame type input."


def testing_main_summary_input():
    assert summary_stats(None) == "Please provide valid DataFrame type input."


def testing_main_visualize_input():
    assert (
        visualize_data(None, None, None) == "Please provide valid DataFrame type input."
    )
