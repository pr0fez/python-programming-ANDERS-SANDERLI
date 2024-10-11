# libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

# global variables
read_path = os.path.dirname(__file__) + "/unlabelled_data.csv"
write_path = os.path.dirname(__file__) + "/labelled_data.csv"
K = -1
X = np.linspace(-10, 10)
M = 0


def read_file(filename):                        # returns df, a dataframe with columns x and y
    
    df = pd.read_csv(filename, header = None)
    df.columns = ["x", "y"]
    
    return df


def classifier(df, K, M):                       # returns lbl, a list of labels
    
    lbl = []

    for i in range(len(df)):
        x = df.iloc[i, 0]
        y = K * x + M
        if df.iloc[i, 1] < y:
            lbl.append(0)
        else:
            lbl.append(1)
    
    return lbl


def write_file(df, lbl):                        # returns df_l, a dataframe with columns x, y, label
    
    df_l = df.copy()
    df_l["label"] = lbl
    df_l.to_csv(write_path, index = False, header = False)

    return df_l


def create_figure(df):                          # returns ax, a plot object

    fig, ax = plt.subplots()                                                # figsize=(9, 9) såg nice ut

    # ax.axis("equal")
    ax.axhline(y = 0, color = "lightseagreen", linewidth = 0.5, zorder = 2)
    ax.axvline(x = 0, color = "lightseagreen", linewidth = 0.5, zorder = 2)

    max_limit = max(abs(df.values.min()), abs(df.values.max()))             # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    ax.set_xlim(-max_limit - 0.5, max_limit + 0.5)                          # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    ax.set_ylim(-max_limit -0.5 , max_limit + 0.5)                          # dessa rader fick jag från Claude, behöver dubbelkollas. gör att plot center är origo
    
    ax.set_title("A scatter plot of the dataframe")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.grid(True, color="gainsboro", linestyle="dashed", zorder=1)

    return ax


def plot_line(ax, X, K, M):                     # plots a decision boundary

    Y = K * X + M
    ax.plot(X, Y, color = "paleturquoise", label = (f"y = {K}x + {M}"), linewidth = 3, zorder = 2)
    ax.fill_between(X, Y, ax.get_ylim()[1], color='aquamarine', alpha=0.25, zorder=0)
    ax.fill_between(X, Y, ax.get_ylim()[0], color='turquoise', alpha=0.15, zorder=0)
    ax.legend(loc = "upper left")


def plot_scatter(ax, df_l):                     # plots a scatter plot with labels

    ax.scatter([], [], marker = "h", color = "aquamarine", edgecolors = "lightseagreen", label = "class 0", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)
    ax.scatter([], [], marker = "H", color = "turquoise", edgecolors = "teal", label = "class 1", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)

    for i in range(len(df_l)):
        if df_l.iloc[i, 2] == 0:
            ax.scatter(df_l.iloc[i, 0], df_l.iloc[i, 1], marker = "h", color = "aquamarine", edgecolors = "lightseagreen", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)
        if df_l.iloc[i, 2] == 1:
            ax.scatter(df_l.iloc[i, 0], df_l.iloc[i, 1], marker = "H", color = "turquoise", edgecolors = "teal", linewidth = 1, s = 50, alpha = 0.75, zorder = 3)

    ax.legend(loc = "upper left")


# main
if __name__ == "__main__":
    
    import matplotlib
    matplotlib.use('qt5agg')

    dataframe = read_file(read_path)
    labels = classifier(dataframe, K, M)
    dataframe_labelled = write_file(dataframe, labels)

    ax = create_figure(dataframe)
    plot_line(ax, X, K, M)
    plot_scatter(ax, dataframe_labelled)
    plt.show()