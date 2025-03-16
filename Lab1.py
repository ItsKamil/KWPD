import numpy as np

def arr_game (a: np.ndarray, minimalize: bool):
    if minimalize:
        strategy_a = min(np.max(a, axis = 1))
        strategy_b = max(np.min(a, axis = 0))
    else:
        strategy_b = min(np.max(a, axis = 0))
        strategy_a = max(np.min(a, axis = 1))

    if strategy_a == strategy_b:
        saddle_point = True
    else:
        saddle_point = False
    return strategy_a, strategy_b, saddle_point


A = np.array([[-2, 3, 5],
              [3, -1, 0],
              [2, 0, -1],
              [-3, 2, 1]])
option_one = True
option_two = False

(sa, sb, sp) = arr_game(A, option_one)

assert sa == 2, "sa not 2"
assert sb == -1, "sb not -1"
assert sp == False, "sp not false"

print(sa, sb, sp)

(sa, sb, sp) = arr_game(A, option_two)

assert sa == -1, "sa not -1"
assert sb == 3, "sb not 3"
assert sp == False, "sp not false"

print(sa, sb, sp)




