import matplotlib.pyplot as plt


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
