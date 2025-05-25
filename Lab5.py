import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def differential(t, a, V, C):
    return 0.5 * a * (1 - a) * (V - a * C)

# Zyski i koszty
V, C = 2, 1

initial_conditions = [0.15, 0.5, 0.8]

t_span = (0, 40)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

plt.figure(figsize=(10, 6))
for a0 in initial_conditions:
    sol = solve_ivp(differential, t_span, [a0], args=(V, C), t_eval=t_eval, vectorized=True)
    plt.plot(sol.t, sol.y[0], label=f"a(0) = {a0}")

plt.title(f"Przebieg proporcji jastrzębi do gołębi dla V = {V}, C = {C}")
plt.xlabel("t")
plt.ylabel("a(t)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
