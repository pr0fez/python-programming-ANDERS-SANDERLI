import numpy as np
import matplotlib.pyplot as plt


def Euclidean_distance_2D(P, Q):
    distance = np.sqrt((np.square(P[0] - Q[0])) + (np.square(P[1] - Q[1])))
    return float(distance)


def distance_listing(T, D):
    distance_list_2D = []
    distance_list = []
    for p in testpoints_arr:                                        # borde vara T, men då kraschar allt
        for q in datapoints_arr:                                    # borde vara D, men då kraschar allt
            distance = Euclidean_distance_2D(p, q[:2])
            distance_list.append(distance)
        distance_list_2D.append(distance_list)
    return distance_list_2D


def classification(T, D):
    pokémon_dict = {0: "Pichu", 1: "Pikachu"}
    distance_list_2D = distance_listing(T, D)
    for i in range(len(distance_list_2D)):
        nearest_distance = 1000
        nearest_class = None
        nearest_coordinate = None
        for index, distance in enumerate(distance_list_2D[i]):
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_class = D[index][2]
                nearest_coordinate = D[index][:2]
        print(f"Sample with (width, height): {T[i]} classified as {pokémon_dict[nearest_class]}.") #Closest to {nearest_coordinate}


#########################

path_datapoints = "/home/albot/coding/repos/python-programming-ANDERS-SANDERLI/Data/datapoints.txt"

with open(path_datapoints, "r") as dp:
    temp_list = []
    lines = dp.readlines()
    for row in lines[1:]:
        row = row.strip().split(", ")
        temp_list.append(row)
        datapoints_arr = np.array(temp_list, dtype=float)

#########################

for x, y, z in datapoints_arr:
    if z == 0:
        plt.scatter(x, y, color="black", zorder=2)
    else:
        plt.scatter(x, y, color="gold", zorder=3)

plt.legend(["Pichu", "Pikachu"], loc="upper left")
plt.grid(True, color="gainsboro", linestyle="dashed", zorder=1)

#########################

path_testpoints = "/home/albot/coding/repos/python-programming-ANDERS-SANDERLI/Data/testpoints.txt"

with open(path_testpoints, "r") as tp:
    temp_list = []
    lines = tp.readlines()
    for row in lines[1:]:
        row = row[3:].strip().split(") ")
        for pair in row:
            pair = pair.strip("()").split(", ")
            temp_list.append(pair)
            testpoints_arr = np.array(temp_list, dtype=float)

#########################

classification(testpoints_arr, datapoints_arr)