# libraries
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('qt5agg')
import os

# global variables
read_path = os.path.dirname(__file__) + "/unlabelled_data.csv"
write_path = os.path.dirname(__file__) + "/labelled_data.csv"
K = -1
X = np.linspace(-10, 10, 600)
M = 0


def read_file(filename):                        # returns df, a dataframe with columns x and y
    
    df = pd.read_csv(filename, header = None)
    df.columns = ["x", "y"]
    
    return df


def create_figure(df):                          # returns ax, a plot object

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_facecolor("azure")

    ax.axis("equal")
    ax.axhline(y = 0, color = "lightseagreen", linewidth = 0.5, zorder = 2)
    ax.axvline(x = 0, color = "lightseagreen", linewidth = 0.5, zorder = 2)

    max_limit = max(abs(df.values.min()), abs(df.values.max()))             # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    ax.set_xlim(-max_limit - 0.5, max_limit + 0.5)                                      # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    ax.set_ylim(-max_limit -0.5 , max_limit + 0.5)                                      # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    
    ax.set_title("A scatter plot of the dataframe")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.grid(True, color="gainsboro", linestyle="dashed", zorder=1)

    return ax


def plot_line(X, K, M):                         # plots a regression line

    Y = K * X + M
    ax.plot(X, Y, color = "paleturquoise", label = (f"y = {K}x + {M}"), linewidth = 3, zorder = 1)
    ax.legend(loc = "upper left")


def classifier(df, K, M):                       # returns lbl, a list of labels
    
    lbl = []

    for i in range(len(df)):
        x = df.iloc[i][0]
        y = K * x + M
        if df.iloc[i][1] < y:
            lbl.append(0)
        else:
            lbl.append(1)
    
    return lbl


def plot_scatter(df, lbl):                      # plots a scatter plot with labels

    ax.scatter([], [], color = "aquamarine", edgecolors = "lightseagreen", label = "class 0", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)
    ax.scatter([], [], marker = "H", color = "turquoise", edgecolors = "teal", label = "class 1", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)

    for i in range(len(df)):
        if lbl[i] == 0:
            ax.scatter(df.iloc[i][0], df.iloc[i][1], color = "aquamarine", edgecolors = "lightseagreen", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)
        if lbl[i] == 1:
            ax.scatter(df.iloc[i][0], df.iloc[i][1], marker = "H", color = "turquoise", edgecolors = "teal", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)

    ax.legend(loc = "upper left")


def write_file(df, lbl):                        # returns df_l, a dataframe with columns x, y, label
    
    df_l = df.copy()
    df_l["label"] = lbl
    df_l.to_csv(write_path, index = False, header = False)

    return df_l


# main
if __name__ == "__main__":
    dataframe = read_file(read_path)
    ax = create_figure(dataframe)
    plot_line(X, K, M)
    labels = classifier(dataframe, K, M)
    plot_scatter(dataframe, labels)
    dataframe_labelled = write_file(dataframe, labels)
    plt.show()




# NOTES
# 1. läs fil
# 2. initiera globala variabler 
# 3. klassificera
# 4. skriv fil
# 5. plotta graf, punkter, linje


# FIX
# ändra linspace till att vara len(dataframe) i stället för 600 - dubbelkolla bara så att inte headers räknas med
# ändra ordningen så att den matchar NOTES