import numpy as np
import matplotlib.pyplot as plt

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