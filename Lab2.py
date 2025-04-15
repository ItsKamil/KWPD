import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

def mixed_strat2v2(a: np.ndarray, D2: bool):

#if D2 false -> D2 clean strategies
#if D2 true -> D1 clean strategies
    if D2 == False:
        a = np.transpose(a)

    x = np.linspace(0, 1, 100)
    if (a.shape[1] != 2):
        print("Wrong size of array")
        return None



    pointz1x1 , pointz1y1 = 1, a[1, 0]
    pointz1x2, pointz1y2 = 0, a[0, 0]

    pointz2x1 , pointz2y1 = 1, a[1,1]
    pointz2x2, pointz2y2 = 0, a[0, 1]

    #functions
    k1 = (pointz1y2 - pointz1y1) / (pointz1x2 - pointz1x1)
    k2 = (pointz2y2 - pointz2y1) / (pointz2x2 - pointz2x1)

    j1 = pointz1y1 - k1 * pointz1x1
    j2 = pointz2y1 - k2 * pointz2x1

    z1 = k1 * x + j1
    z2 = k2 * x + j2


    idx = np.argmin(np.abs(z1 - z2))
    saddle_p = x[idx]
    saddle_value = z1[idx]

    plt.scatter(saddle_p, saddle_value, color='red', s=50, label=f"Saddle point", zorder=5)  #
    #plt.plot(saddle_p, saddle_value, 'g*')
    plt.plot(x, z1, label='z1')
    plt.plot(x, z2, label='z2')
    if D2 == False:
        plt.title('D1 clean strategies')
    else:
        plt.title('D2 clean strategies')
    plt.grid(True)
    plt.show()

    return saddle_p,saddle_value #round(saddle_p,1), round(saddle_value,1)

arr = np.array([[4, -3],
                [2, 5]])

print("D2 clean strategies -> (saddle point, saddle value) =", mixed_strat2v2(arr, True))
print("D1 clean strategies -> (saddle point, saddle value) =", mixed_strat2v2(arr, False))

# zad 3

def linear_prog(A, minimize):
        if minimize: 
            A_ub = A.T
            b_ub = [1] * A.shape[1]
            c = [-1] * A.shape[0]
            bounds = [(0, None)] * A.shape[0]
            nr = 1
            symb = "y"
        else:
            A_ub = -A
            b_ub = [-1] * A.shape[0]
            c = [1] * A.shape[1]
            bounds = [(0, None)] * A.shape[1]
            nr = 2
            symb = "z"
            
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

        if res.success:
            w = res.x
            Sm = 1/sum(w)
            strategy = w*Sm
            result = f"Strategia mieszana gracza D{nr}: " + ", ".join(
            [f"{symb}{i} = {p:.4f}" for i, p in enumerate(strategy, start=1)]
            )
            print(result)
            print(f"Wynik gry (Sm): {Sm:.4f}")
        else:
            print("Nie udało się znaleźć rozwiązania.")

print("---Zadanie 3---")

A = np.array(
    [[4, -3, 0],
     [2, 5, 1]]
     )

linear_prog(A,True)
linear_prog(A,False)


# zad 4

print("---Zadanie 4---")

A = np.array([
    [5, 3, 7, 6, 4, 2],
    [8, 6, 1, 3, 5, 7],
    [7, 2, 9, 4, 5, 6],
    [10, 5, 3, 9, 6, 7],
    [9, 8, 4, 6, 11, 7],
    [11, 9, 5, 8, 7, 6]
])

linear_prog(A,True)
linear_prog(A,False)