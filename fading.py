import cmath
import graphing
import numpy as np

j = complex(0, 1)

def get_iteration_values_for_div_equations(t, c0t, c1t, omega_r, dw, gamma, e1, e2, h_bar):
    c0r = -omega_r * cmath.exp(complex(0, dw * t)) * c1t / j - complex(0, gamma) * complex(0, -e1 / h_bar * t) * c0t
    c1r = -omega_r * cmath.exp(complex(0, -dw * t)) * c0t / j - complex(0, gamma) * complex(0, -e2 / h_bar * t) * c1t
    return c0r, c1r


def solve_equations(t_stop, dt, c0, c1, omega_r, dw, gamma, e1, e2, h_bar):
    time = np.arange(0, t_stop, dt)
    c0_v = [c0]
    c1_v = [c1]
    for i in range(1, len(time)):
        c0_r, c1_r = get_iteration_values_for_div_equations(time[i], c0_v[i - 1], c1_v[i - 1], omega_r, dw, gamma, e1, e2, h_bar)
        c0_v.append(c0_v[i - 1] + c0_r * dt)
        c1_v.append(c1_v[i - 1] + c1_r * dt)

    return time, c0_v, c1_v
