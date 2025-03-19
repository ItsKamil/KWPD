import numpy as np

def arr_game(a: np.ndarray):
    max_in_rows = [max(row) for row in a]    # Maksymalne wartości w wierszach
    min_in_cols = [min(col) for col in a.T]  # Minimalne wartości w kolumnach

    SL_D1 = min(max_in_rows)  # Najmniejsza wartość spośród największych wierszowych
    SL_D2 = max(min_in_cols)  # Największa wartość spośród najmniejszych kolumnowych

    STR_D1 = np.argmin(max_in_rows)
    STR_D2 = np.argmax(min_in_cols)

    if(SL_D1 == SL_D2):
        PS = True
    else:
        PS = False

    return SL_D1, SL_D2, STR_D1 + 1, STR_D2 + 1, PS

A = np.array([[4, 0, -1],
              [0, -1, 3],
              [1, 2, 1],
              [3, 1, 0]])
option_one = True
option_two = False

(sa, sb, str1, str2, ps) = arr_game(A)

print(
      "Strategia gracza D1: " + str(str1) + "\n" +
      "Strategia gracza D2: " + str(str2) + "\n \n" +
      "Poziom bezpieczenstwa gracza D1: " + str(sa) + "\n" +
      "Poziom bezpieczenstwa gracza D2: " + str(sb) + "\n \n" +
      "Punkt siodlowy: " + str(ps)
)




