import no_fading
import fading
import graphing
import numpy as np

t_max = 50
dt = 1e-3
w = 0.1
gamma = 1e-3

d_12 = 1.0
e0 = 1.0
e1 = 1.0
e2 = 1.1

h_bar = 1

w0 = (e2 - e1) / h_bar
dw = w - w0
omega_r = d_12 * e0 / (h_bar * 2)

starting_points = [
    [complex(1, 0), complex(0, 0)],
    [complex(0, 0), complex(1, 0)],
    [complex(0.5 ** 0.5, 0), complex(0.5 ** 0.5, 0)]
]


def test_starting_point():
    for point in starting_points:
        title = "C1(0)=" + str(round(point[0].real, 3)) + " C2(0) = " + str(round(point[1].real, 3))
        time, c1, c2 = fading.solve_equations(t_max, dt, point[0], point[1], omega_r, dw, gamma, e1, e2, h_bar)
        graphing.make_graph(time, c1, c2, "Fading " + title)
        time, c1, c2 = no_fading.solve_equations(t_max, dt, point[0], point[1], omega_r, dw, gamma, e1, e2, h_bar)
        graphing.make_graph(time, c1, c2, "No fading " + title)


def test_delta_dependency():
    point = starting_points[0]
    ws = np.arange(0, 2, 0.3)
    for wl in ws:
        dwl = wl - w0
        title = "dw = " + str(round(dwl, 3))
        time, c1, c2 = fading.solve_equations(t_max, dt, point[0], point[1], omega_r, dwl, gamma, e1, e2, h_bar)
        graphing.make_graph(time, c1, c2, "Fading " + title)
        time, c1, c2 = no_fading.solve_equations(t_max, dt, point[0], point[1], omega_r, dwl, gamma, e1, e2, h_bar)
        graphing.make_graph(time, c1, c2, "No fading " + title)


def test_gamma_dependency():
    point = starting_points[0]
    gammas = [1e-3, 0.7, 1e3]
    for gammal in gammas:
        title = "gamma = " + str(round(gammal, 3))
        time, c1, c2 = fading.solve_equations(t_max, dt, point[0], point[1], omega_r, dw, gammal, e1, e2, h_bar)
        graphing.make_graph(time, c1, c2, "Fading " + title)


def draw_graphs_no_fading():
    for i in range(1, 4):
        time, c1, c2 = no_fading.solve_equations(10, 1e-1, starting_points[i - 1][0], starting_points[i - 1][1],
                                                 omega_r, dw, gamma, e1, e2, h_bar)
        graphing.draw_sphere(time, c1, c2, "No_fading" + str(i))


def draw_graphs_with_fading():
    for i in range(1, 4):
        time, c1, c2 = fading.solve_equations(20, 1e-1, starting_points[i - 1][0], starting_points[i - 1][1], omega_r,
                                              dw, 1e-1, e1, e2, h_bar)
        graphing.draw_sphere(time, c1, c2, "Fading" + str(i))


# test_starting_point()
# test_delta_dependency()
# test_gamma_dependency()
draw_graphs_no_fading()
draw_graphs_with_fading()
