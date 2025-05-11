
import networkx as nx
import matplotlib.pyplot as plt

import numpy as np


import math



def draw_decision_tree(values1, values2=None):
    if values2 is not None and len(values1) != len(values2):
        raise ValueError("wrong size")
    n = len(values1)
    if n == 0 or (n & (n - 1)) != 0:
        raise ValueError("wrong size")

    depth = int(math.log2(n))

    fig, ax = plt.subplots(figsize=(14, 2 + depth))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    levels_y = [1.0 - i * (0.9 / (depth + 1)) for i in range(depth + 1)]

    def draw_node(text, x, y, color="lightblue"):
        ax.text(x, y, text, ha='center', va='center',
                bbox=dict(boxstyle="round", facecolor=color))

    def connect(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], 'k-')

    def draw_subtree(x_center, level, idx):
        if level == depth:
            if values2 is not None:
                label = f"{values1[idx]} | {values2[idx]}"
            else:
                label = f"{values1[idx]}"
            draw_node(label, x_center, levels_y[level], color="lightgreen")
            return

        node_name = (level+1)%2
        if node_name == 0: node_name = 2

        draw_node(f"D{node_name}", x_center, levels_y[level])
        offset = 1 / (2 ** (level + 2))
        left_x = x_center - offset
        right_x = x_center + offset

        connect(x_center, levels_y[level], left_x, levels_y[level + 1])
        connect(x_center, levels_y[level], right_x, levels_y[level + 1])

        draw_subtree(left_x, level + 1, 2 * idx)
        draw_subtree(right_x, level + 1, 2 * idx + 1)

    draw_subtree(0.5, 0, 0)
    plt.show()


def arr_game(a: np.ndarray):
    max_in_rows = [max(row) for row in a]    # Maksymalne wartości w wierszach
    min_in_cols = [min(col) for col in a.T]  # Minimalne wartości w kolumnach

    SL_D1 = min(max_in_rows)  # Najmniejsza wartość spośród największych wierszowych
    SL_D2 = max(min_in_cols)  # Największa wartość spośród najmniejszych kolumnowych

    STR_D1 = (np.where(max_in_rows == SL_D1)[0] + 1).tolist()
    STR_D2 = (np.where(min_in_cols == SL_D2)[0] + 1).tolist()

    if(SL_D1 == SL_D2):
        PS = True
    else:
        PS = False

    return SL_D1, SL_D2, STR_D1, STR_D2, PS

def nash(a: np.ndarray, b: np.ndarray):

    if (a.shape != b.shape) or (a.shape[1] != a.shape[0]):
        print("Wrong size of arrays")
        return None
    nashPoints = []
    nashValues = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            tempA = a[:, j]
            tempB = b[i]
            if a[i, j] == min(tempA) and b[i,j] == min(tempB):
                nashPoints.append((i, j))
                nashValues.append((a[i, j], b[i, j]))

    return nashPoints, nashValues


def decision_tree(a: np.ndarray, K: int):
    number = pow(4,K)
    if a.shape[1] != number:
        print("Wrong size of array")
        print(a.shape[1])
        return None

    for _ in range(K):
        cases = int(a.shape[1]/4)
        newA= np.array_split(a,cases, axis=1)

        branches = len(newA)

        list_of_arrays = [np.zeros((2,2)) for _ in range(branches)]

        for i, x in enumerate(newA):
            list_of_arrays[i][0][0] = x[0, 0]
            list_of_arrays[i][0][1] = x[0, 1]
            list_of_arrays[i][1][0] = x[0, 2]
            list_of_arrays[i][1][1] = x[0, 3]

        y = np.zeros((1,branches))

        for x in range(branches):
            result=arr_game(list_of_arrays[x])
            y[0,x]=result[1]

        a = y
    return a

def decision_tree_nash(a: np.ndarray, b: np.ndarray, K: int):
    number = pow(4,K)
    if a.shape[1] != number:
        print("Wrong size of array")
        print(a.shape[1])
        return None
    if b.shape[1] != number:
        print("Wrong size of array")
        print(a.shape[1])
        return None

    for _ in range(K):
        cases = int(a.shape[1]/4)
        newA= np.array_split(a,cases, axis=1)
        newB = np.array_split(b,cases, axis=1)

        branches = len(newA)

        list_of_arraysA = [np.zeros((2,2)) for _ in range(branches)]

        for i, x in enumerate(newA):
            list_of_arraysA[i][0][0] = x[0, 0]
            list_of_arraysA[i][0][1] = x[0, 1]
            list_of_arraysA[i][1][0] = x[0, 2]
            list_of_arraysA[i][1][1] = x[0, 3]

        list_of_arraysB = [np.zeros((2, 2)) for _ in range(branches)]

        for i, x in enumerate(newB):
            list_of_arraysB[i][0][0] = x[0, 0]
            list_of_arraysB[i][0][1] = x[0, 1]
            list_of_arraysB[i][1][0] = x[0, 2]
            list_of_arraysB[i][1][1] = x[0, 3]

        y = np.zeros((1,branches))
        z = np.zeros((1, branches))

        for x in range(branches):
            result=nash(list_of_arraysA[x], list_of_arraysB[x])
            nash_values =result[1]

            if nash_values:
                y[0, x] = nash_values[0][0]
                z[0, x] = nash_values[0][1]
            else:
                y[0, x] = 0
                z[0, x] = 0

        a = y
        b = z

    return a, b




dane = [-2, 0, -1, 3, 0, 7, -1, 4, -1, -2, 2, 1, 4, 3, 2, 1]
dane2 =  [10, 2, 3, 1, 2, 0, -1, -2, 0, -1, 2, -4, -3, 0, 2, 1]
a11 = np.array(dane)
a1 = np.array(dane).reshape((1,16))
a12 = np.array(dane2)
a2 = np.array(dane2).reshape((1,16))
ax =decision_tree(a1, 2)

ay = decision_tree_nash(a1,a2, 2)

print(ax)
print("zad2" + str(ay))


draw_decision_tree(dane)