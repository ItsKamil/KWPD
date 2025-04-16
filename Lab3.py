import numpy as np


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


def hierarchy(a: np.ndarray, b: np.ndarray, leader: bool):
    # if leader == true -> D1 leader
    # if leader == false -> D2 leader
    if leader == False:
        c=b
        b=a
        a=c
        a = np.transpose(a)
        b = np.transpose(b)
    if (a.shape != b.shape) or (a.shape[1] != a.shape[0]):
        print("Wrong size of arrays")
        return None
    k=0
    rationalPoints = []
    rationalValues = []
    tempPoints = []


    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            tempA = a[:, j]
            tempB = b[i]
            if b[i,j] == min(tempB) and np.sum(tempB == np.min(tempB)) <2:
                rationalPoints.append((i, j))
                rationalValues.append((a[i, j], b[i, j]))
            elif b[i,j] == min(tempB):
                k=i
                tempPoints.append((j, a[i, j]))
    if k!=0:
        best_j, _ = max(tempPoints, key=lambda x: x[1])
        rationalPoints.append((k, best_j))
        rationalValues.append((a[k, best_j], b[k, best_j]))

    min_value = min(x[0] for x in rationalValues)

    strategy = [i for i, x in enumerate(rationalValues) if x[0] == min_value]


    selectedPoints = [rationalPoints[i] for i in strategy]
    selectedValues = [rationalValues[i] for i in strategy]

    return selectedPoints, selectedValues





arrA = np.array([[4, 3, 1, 7],
                [-1, 3, 2, 1],
                 [1, 2, 3, 0],
                 [4, 5, 3, -1]
                 ])
arrB = np.array([[2, 3, 4, 8],
                [-2, 1, 3, 2],
                 [0, -2, 4, -2],
                 [4, 3, 2, 5]
                 ])


leader = True
follower = False

print("Nash points and values -> (Nash points, Nash values) =", nash(arrA, arrB))
print("Hierarchy points and values -> (Hierarchy points, Hierarchy values) =", hierarchy(arrA, arrB, leader))
print("Hierarchy points and values -> (Hierarchy points, Hierarchy values) =", hierarchy(arrA, arrB, follower))
