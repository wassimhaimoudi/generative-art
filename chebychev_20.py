if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    def chebyshev_poly(n, x):
        if n == 0:
            return np.ones_like(x)
        elif n == 1:
            return x
        else:
            return 2 * x * chebyshev_poly(n - 1, x) - chebyshev_poly(n - 2, x)

    x = np.linspace(-1, 1, 1000)
    colors = plt.cm.viridis(np.linspace(0, 1, 20))

    plt.figure(figsize=(16, 9))

    for i in range(20):
        y = chebyshev_poly(i, x)
        plt.plot(x, y, color=colors[i])
    plt.show()
