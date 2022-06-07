import no_fading
import fading
import graphing

t_max = 50
dt = 1e-3
w = 0.1
gamma = 1e-2

d_12 = 1.0
e0 = 1.0
e1 = 1.0
e2 = 1.1

h_bar = 1

w0 = (e2 - e1) / h_bar
dw = w - w0
omega_r = d_12 * e0 / (h_bar * 2)


time, c1, c2 = fading.solve_equations(t_max, dt, complex(0, 1), complex(0, 0), omega_r, dw, gamma, e1, e2, h_bar)
graphing.make_graph(time, c1, c2)
time, c1, c2 = no_fading.solve_equations(t_max, dt, complex(0, 1), complex(0, 0), omega_r, dw, gamma, e1, e2, h_bar)
graphing.make_graph(time, c1, c2)

