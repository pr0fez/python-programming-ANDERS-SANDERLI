# importing dependencies
import numpy as np
import matplotlib.pyplot as plt


# functions
def read_files(pT, pD):                               # returns testpoints_arr, datapoints_arr
    
    with open(pT, "r") as tp:
        temp_list = []
        lines = tp.readlines()
        for row in lines[1:]:
            row = row[3:].strip().split(") ")
            for pair in row:
                pair = pair.strip("()").split(", ")
                temp_list.append(pair)
                testpoints_arr = np.array(temp_list, dtype=float)

    with open(pD, "r") as dp:
        temp_list = []
        lines = dp.readlines()
        for row in lines[1:]:
            row = row.strip().split(", ")
            temp_list.append(row)
            datapoints_arr = np.array(temp_list, dtype=float)
    
    return testpoints_arr, datapoints_arr


def scatter_points(T, D):                       # returns nothing. prints a scatter plot

    # this trick with scatter came from Copilot, highlighting the code and prompting: "I want the legend to only show the three alternatives, not each dot."
    plt.scatter([], [], color="black", label="Pichu", edgecolors="black", linewidth=1, s=75, alpha=0.75)
    plt.scatter([], [], color="gold", label="Pikachu", edgecolors="black", linewidth=1, s=75, alpha=0.75)
    plt.scatter([], [], color="dodgerblue", label="Test points", edgecolors="black", linewidth=1, s=75, alpha=0.75)

    for x, y in T:
        plt.scatter(x, y, color="dodgerblue", zorder=4, edgecolors="black", linewidth=1, s=75, alpha=0.75)

    for x, y, z in D:
        if z == 0:
            plt.scatter(x, y, color="black", zorder=2, edgecolors="black", linewidth=1, s=75, alpha=0.75)
        else:
            plt.scatter(x, y, color="gold", zorder=3, edgecolors="black", linewidth=1, s=75, alpha=0.75)

    plt.legend(loc="upper left")
    plt.grid(True, color="gainsboro", linestyle="dashed", zorder=1)
    plt.show()


def Euclidean_distance_2D(P, Q):                # returns distance
    distance = np.sqrt((np.square(P[0] - Q[0])) + (np.square(P[1] - Q[1])))
    return float(distance)


def distance_listing(T, D):                     # returns distance_list_2D
    distance_list_2D = []
    for p in T:
        distance_list = []
        for q in D:
            distance = Euclidean_distance_2D(p, q[:2])
            distance_list.append(distance)
        distance_list_2D.append(distance_list)
    return distance_list_2D


def nearest_neighbour(T, D):                    # returns nothing. ######prints classification
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
        print(f"Sample with (width, height): {T[i]} classified as {pokémon_dict[nearest_class]}.")


def user_testpoint():                           # returns T_user

    T_user = []

    while True:

        try:
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))

            if width < 0 or height < 0:
                print("Width and height must be positive.")
                continue

            T_user.append([width, height])
            break

        except ValueError as err:
            print(f"An error occured: '{err}'")
    
    return T_user


def k_nearest_neighbour(T, D, k, printing):        # returns class_guesses_arr, prints classification if printing == True
    
    temp_list_T = []
    temp_list_class = []
    pokémon_dict = {0: "Pichu", 1: "Pikachu"}    

    distance_list_2D = distance_listing(T, D)

    sorted_distances = []
    for list in distance_list_2D:
        temp = list.copy()
        temp.sort()
        sorted_distances.append(temp[:k])
    
    sorted_indices = []
    for i in range(len(sorted_distances)):
        temp_list = []
        for distance in sorted_distances[i]:
            index = distance_list_2D[i].index(distance)
            temp_list.append(index)
        sorted_indices.append(temp_list)
    
    sorted_class = []
    for i in range(len(sorted_indices)):
        temp_list = []
        for index in sorted_indices[i]:
            label = D[index][2]
            temp_list.append(float(label))
        sorted_class.append(temp_list)
    
    for i in range(len(sorted_class)):
        num_pichu = 0
        num_pikachu = 0
        for j in sorted_class[i]:
            j = int(j)
            if j == 0:
                num_pichu += 1
            else:
                num_pikachu += 1

        # print classification and make a list of same guesses
        if num_pichu > num_pikachu:
            if printing == True:
                print(f"Sample with (width, height): {T[i]} classified as {pokémon_dict[0]}.")
            temp_list_T.append(T[i])
            temp_list_class.append([0.0])
        else:
            if printing == True:
                print(f"Sample with (width, height): {T[i]} classified as {pokémon_dict[1]}.")
            temp_list_T.append(T[i])
            temp_list_class.append([1.0])
    
    class_guesses_arr = np.hstack((temp_list_T, temp_list_class))

    
    return class_guesses_arr


def new_points(D):                              # returns new_testpoints_arr, new_testpoints_key_arr, new_datapoints_arr

    # variables
    new_datapoints_arr = D.copy()
    new_testpoints_list = []
    pichu_points = []
    pikachu_points = []

    # separating the two classes
    for i in range(len(new_datapoints_arr)):
        if new_datapoints_arr[i][2] == 0:
            pichu_points.append(new_datapoints_arr[i])
        else:
            pikachu_points.append(new_datapoints_arr[i])
    
    pichu_points_arr = np.array(pichu_points)
    pikachu_points_arr = np.array(pikachu_points)

    # choosing new testpoints
    for i in range(len(pichu_points_arr)):
        if len(new_testpoints_list) < 50:
            temp_pichu = []
            temp_pikachu = []
            np.random.shuffle(pichu_points_arr)
            np.random.shuffle(pikachu_points_arr)
            temp_pichu = pichu_points_arr[0]                # plocka index noll
            temp_pikachu = pikachu_points_arr[0]
            new_testpoints_list.append(temp_pichu)
            new_testpoints_list.append(temp_pikachu)
            pichu_points_arr = pichu_points_arr[1:]         # nya filen utan index noll
            pikachu_points_arr = pikachu_points_arr[1:]
        else:
            break
    
    new_testpoints_key_arr = np.array(new_testpoints_list)
    np.random.shuffle(new_testpoints_key_arr)
    np.random.shuffle(pichu_points_arr)
    np.random.shuffle(pikachu_points_arr)

    # combining the two classes
    new_datapoints_arr = np.vstack((pichu_points_arr, pikachu_points_arr))
    np.random.shuffle(new_datapoints_arr)

    # removing the class labels from the testpoints
    new_testpoints_list = []
    for i in range(len(new_testpoints_key_arr)):
        temp_list = []
        temp_list = new_testpoints_key_arr[i][:2]
        new_testpoints_list.append(temp_list)
    
    new_testpoints_arr = np.array(new_testpoints_list) 


    return new_testpoints_arr, new_testpoints_key_arr, new_datapoints_arr


def accuracy(key, guess):                       # returns accuracy_score, accuracy_dict (TP, TN, FP, FN)

    # variables
    accuracy_dict = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}

    # comparison of key and guesses
    for i in range(len(key)):
        if key[i][2] == 1:
            if guess[i][2] == 1:
                accuracy_dict["TP"] += 1
            else:
                accuracy_dict["FN"] += 1
        else:
            if guess[i][2] == 0:
                accuracy_dict["TN"] += 1
            else:
                accuracy_dict["FP"] += 1
    
    accuracy_score = (accuracy_dict["TP"] + accuracy_dict["TN"]) / (accuracy_dict["TP"] + accuracy_dict["TN"] + accuracy_dict["FP"] + accuracy_dict["FN"])

    return accuracy_score, accuracy_dict


def iterations(times):                          # returns nothing. prints accuracy table and plot

    # variables
    printing = False
    score_over_time = []
    score_dict = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}
    x = []

    # run the whole program multiple times
    for i in range(times):
        T_new, T_new_key, D_new = new_points(D)
        T_guess = k_nearest_neighbour(T_new, D_new, k, printing)
        score, temp_dict = accuracy(T_new_key, T_guess)
        score_over_time.append(score*100)
        for key in temp_dict:
            if key in score_dict:
                score_dict[key] += temp_dict[key]
        x.append(i+1)

    # plot the accuracy for each iteration
    plt.plot(x, score_over_time, color="firebrick", linewidth=5, zorder=2)
    plt.title("Pokémon classification accuracy over time")
    plt.xlabel("Iterations")
    plt.ylabel("Accuracy (%)")
    # plt.xticks(np.arange(1, times + 1))
    plt.grid(True, color="gainsboro", linestyle="dashed", zorder=1)
    plt.show()

    # variables
    total_score = sum(score_over_time)
    title = f"Accuracy table over {times} iterations"
    average_score = f"Average accuracy: {total_score / times:.2f} %"
    outer_border = "+---------------------------------------------------+"
    inner_border = "|-------------------|----------------|--------------|"
    column_2 = "----------------"
    column_3 = "--------------"

    # accuracy table                                                                    # kanske är snyggare utan variabler, i största möjliga mån
    print(f"""
    {outer_border}
    | {title:^{len(outer_border)-4}} |
    {outer_border}
    |                   | Pikachu actual | Pichu actual |
    {inner_border}
    | Pikachu predicted | {score_dict["TP"]:>{len(column_2)-2}} | {score_dict["FP"]:>{len(column_3)-2}} |
    {inner_border}
    | Pichu predicted   | {score_dict["FN"]:>{len(column_2)-2}} | {score_dict["TN"]:>{len(column_3)-2}} |
    {outer_border}
    | {average_score:^{len(outer_border)-4}} |
    {outer_border}
    """)


def menu():                                     # runs the show

    print("Welcome.  \n\nThis is the APCP (Albot Pokémon Classification Program).")
    
    while True:

        print("""\n
    1. Plot the training data and classify pre-loaded samples
    2. Classify a custom sample of your own (using NN)
    3. Classify a custom sample of your own (using KNN)
    4. Randomly choose testpoints and classify those (using KNN)
    5. Option 4 but runs the program ten times and plots accuracy
    6. Exit
        """)
        print("Choose an option: ", end="", flush=True)

        try:
            user_choice = int(input())

            if user_choice == 1:
                print(f"You chose {user_choice}\n\n")
                scatter_points(T, D)
                nearest_neighbour(T, D)

            elif user_choice == 2:
                print(f"You chose {user_choice}\n\n")
                T_user = user_testpoint()
                nearest_neighbour(T_user, D)
                scatter_points(T_user, D)

            elif user_choice == 3:
                print(f"You chose {user_choice}\n\n")
                T_user = user_testpoint()
                printing = True
                k_nearest_neighbour(T_user, D, k, printing)
                scatter_points(T_user, D)

            elif user_choice == 4:
                print(f"You chose {user_choice}\n\n")
                T_new, T_new_key, D_new = new_points(D)
                printing = True
                guesses = k_nearest_neighbour(T_new, D_new, k, printing)
                scatter_points(T_new, D_new)

            elif user_choice == 5:
                print(f"You chose {user_choice}\n\n")
                iterations(times)

            elif user_choice == 6:
                print(f"You chose {user_choice}\n\n")
                print(f"Have a good day.")
                break

            else:
                print("\n\nTry again.")

        except ValueError as err:
            print("\n")
            print(f"An error occured: '{err}'")


# global variables
path_datapoints = "/home/albot/coding/repos/python-programming-ANDERS-SANDERLI/Data/datapoints.txt"
path_testpoints = "/home/albot/coding/repos/python-programming-ANDERS-SANDERLI/Data/testpoints.txt"
T, D = read_files(path_testpoints, path_datapoints)
k = 10
times = 10


# TESTING
menu()


# FIX
# 1. 