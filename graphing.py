import matplotlib.pyplot as plt


def make_graph(x, c1, c2):
    c = []
    c1m = []
    c2m = []
    for i in range(0, len(x)):
        c.append(abs(c2[i]) ** 2 - abs(c1[i]) ** 2)
        c1m.append(abs(c1[i]) ** 2)
        c2m.append(abs(c2[i]) ** 2)

    print(c1)
    print(c2)
    print(c)
    plt.plot(x, c, label="|C2|^2 - |C1|^2")
    plt.plot(x, c1m, label="|C1|^2")
    plt.plot(x, c2m, label="|C2|^2")
    plt.legend()
    plt.show()
