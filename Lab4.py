
import networkx as nx
import matplotlib.pyplot as plt

import numpy as np



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
a1 = np.array(dane).reshape((1,16))
a2 = np.array(dane2).reshape((1,16))
ax =decision_tree(a1, 2)

ay = decision_tree_nash(a1,a2, 2)

print(ax)
print("zad2" + str(ay))


G = nx.Graph()


G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])


plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
plt.title("Przykład grafu z wykorzystaniem networkx")
plt.show()