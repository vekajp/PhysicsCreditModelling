import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
import qutip
import math
import imageio
from pylab import *


def make_graph(x, c1, c2, title=""):
    c = []
    c1m = []
    c2m = []
    c_sum = []
    for i in range(0, len(x)):
        c.append(abs(c2[i]) ** 2 - abs(c1[i]) ** 2)
        c1m.append(abs(c1[i]) ** 2)
        c2m.append(abs(c2[i]) ** 2)
        c_sum.append(abs(c2[i]) ** 2 + abs(c1[i]) ** 2)

    plt.plot(x, c, label="|C2|^2 - |C1|^2")
    plt.plot(x, c_sum, label="|C2|^2 + |C1|^2")
    plt.plot(x, c1m, label="|C1|^2")
    plt.plot(x, c2m, label="|C2|^2")
    plt.legend()
    plt.title(title)
    plt.show()


def get_coordinates(x, c1, c2):
    x, y, z = [], [], []
    for i in range(len(c1)):
        mod = abs(c1[i])
        if mod > 1:
            mod = 1
        if mod < -1:
            mod = -1
        theta = math.acos(mod) * 2
        try:
            value = c1[i].imag / c1[i].real
            fi = math.atan(value)
        except ZeroDivisionError:
            fi = copysign(1, c1[i].imag * c1[i].real) * math.pi / 2
        x.append(math.cos(fi) * math.sin(theta))
        y.append(math.sin(fi) * math.sin(theta))
        z.append(math.cos(theta))
    return x, y, z


def draw_sphere(x, c1, c2, title, save_all=False):
    x, y, z = get_coordinates(x, c1, c2)
    b = qutip.Bloch()
    b.vector_color = ['r']
    b.view = [-40, 30]
    images = []
    length = len(x)
    ## normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0, length)
    colors = cm.cool(nrm(range(length)))  # options: cool, summer, winter, autumn etc.

    ## customize sphere properties ##
    b.point_color = list(colors)  # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = [30]

    for i in range(length):
        b.clear()
        vec = [x[i], y[i], z[i]]
        b.add_vectors(vec)
        b.add_points([x[:i + 1], y[:i + 1], z[: i + 1]])
        if save_all:
            b.save(dirc='tmp')  # saving images to tmp directory
            filename = "tmp/bloch_%01d.png" % i
        else:
            filename = 'temp_file.png'
            b.save(filename)
        images.append(imageio.imread(filename))
    imageio.mimsave("demonstrations/" + title + '.gif', images, duration=0.1)
