import numpy as np
import matplotlib.pyplot as plt
import cmath
import random as rnd

sr = complex(0.1, 0)
delta = 1e-4
gamma = 1e-15


def solve_div_equations(c10, c20, dt, t):
    c1 = [c10]
    c2 = [c20]
    time = np.arange(0, t, dt)
    j = complex(0, 1)

    for i in range(1, len(time)):
        c1.append(c1[i - 1] + (-sr * cmath.exp(delta * time[i - 1] * j) * c2[i - 1] * dt / j))
        c2.append(c2[i - 1] + (-sr * cmath.exp(-delta * time[i - 1] * j) * c1[i - 1] * dt / j))

    return time, c1, c2


def solve_div_equations_with_fading(c10, c20, dt, t):
    c1 = [c10]
    c2 = [c20]
    time = np.arange(0, t, dt)
    j = complex(0, 1)

    for i in range(1, len(time)):
        rnd.seed()
        c = rnd.random()
        c1.append(c1[i - 1] +
                  ((-sr * cmath.exp(complex(0, delta * time[i - 1])) * c2[i - 1] / j + j * gamma / 2 * c10) * dt / j))
        c2.append(c2[i - 1] +
                  ((-sr * cmath.exp(-delta * time[i - 1] * j) * c1[i - 1] - j * gamma / 2 * c20) * dt / j))

    return time, c1, c2


def make_graph(c10, c20, dt, t):
    t, c1, c2 = solve_div_equations(c10, c20, dt, t)
    c = []
    c1m = []
    c2m = []
    for i in range(0, len(t)):
        c.append(abs(c2[i]) ** 2 - abs(c1[i]) ** 2)
        c1m.append(abs(c1[i]) ** 2)
        c2m.append(abs(c2[i]) ** 2)

    print(c1)
    print(c2)
    print(c)
    plt.plot(t, c, label="|C2|^2 - |C1|^2")
    plt.plot(t, c1m, label="|C1|^2")
    plt.plot(t, c2m, label="|C2|^2")
    plt.legend()
    plt.show()


def make_graph_with_fading(c10, c20, dt, t):
    t, c1, c2 = solve_div_equations_with_fading(c10, c20, dt, t)
    c = []
    c1m = []
    c2m = []
    for i in range(0, len(t)):
        c.append(abs(c2[i]) ** 2 - abs(c1[i]) ** 2)
        c1m.append(abs(c1[i]) ** 2)
        c2m.append(abs(c2[i]) ** 2)

    print(c1)
    print(c2)
    print(c)
    plt.plot(t, c, label="|C2|^2 - |C1|^2")
    plt.plot(t, c1m, label="|C1|^2")
    plt.plot(t, c2m, label="|C2|^2")
    plt.legend()
    plt.show()


make_graph(0, 1, 1e-2, 100)
make_graph_with_fading(0, 1, 1e-2, 1000)
