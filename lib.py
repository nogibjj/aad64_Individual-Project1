"""Importing module pandas for my function."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("RiskData_SumScores.csv")


def average(data):
    """ "This is a mean function."""
    result = data.mean()
    result = round(result, 2)
    return result


def med(data):
    """ "This is a median function."""
    result = data.median()
    return result


def standard_deviation(data):
    """ "This is a standard deviation function."""
    result = data.std()
    result = round(result, 2)
    return result


def visualize_data(
    data, x_column, y_column, hue=None, title=None, xlabel=None, ylabel=None
):
    """
    Visualize data from a DataFrame using Seaborn's swarm plot.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        x_column (str): The column to be used for the x-axis.
        y_column (str): The column to be used for the y-axis.
        hue (str): The column to be used for color differentiation.
        title (str, optional): Title for the plot. Defaults to None.
        xlabel (str, optional): Label for the x-axis. Defaults to None.
        ylabel (str, optional): Label for the y-axis. Defaults to None.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=data, x=x_column, y=y_column, hue=hue)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show(block=True)
