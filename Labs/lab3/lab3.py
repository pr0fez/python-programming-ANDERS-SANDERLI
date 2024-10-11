# libraries
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('qt5agg')


def read_file(filename):                        # returns df with columns x and y
    
    df = pd.read_csv(filename, header = None)
    df.columns = ["x", "y"]
    
    return df


def create_figure(df):                          # returns ax plot object

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_facecolor("azure")

    ax.axis("equal")
    ax.axhline(y = 0, color = "lightseagreen", linewidth = 0.5, zorder = 2)
    ax.axvline(x = 0, color = "lightseagreen", linewidth = 0.5, zorder = 2)

    max_limit = max(abs(df.values.min()), abs(df.values.max()))             # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    ax.set_xlim(-max_limit, max_limit)                                      # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    ax.set_ylim(-max_limit, max_limit)                                      # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    
    ax.set_title("A scatter plot of the dataframe")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.grid(True, color="gainsboro", linestyle="dashed", zorder=1)
    # ax.legend(loc = "upper left")

    return ax


def plot_line(X, K, M):                         # plots a regression line

    Y = K * X + M
    ax.plot(X, Y, color = "paleturquoise", label = (f"y = {K}x + {M}"), linewidth = 3, zorder = 1)
    ax.legend(loc = "upper left")
    plt.show()


# function


# other

# global variables
file_path = "/home/albot/coding/repos/python-programming-ANDERS-SANDERLI/Labs/lab3/unlabelled_data.csv"
K = -1
X = np.linspace(-10, 10, 600)
M = 0

# main
dataframe = read_file(file_path)
ax = create_figure(dataframe)
plot_line(X, K, M)