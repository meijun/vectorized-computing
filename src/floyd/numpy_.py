import numpy as np


def floyd(g, n):
    for k in range(n):
        n_n = g[:, k].reshape(n, 1) + g[k, :].reshape(1, n)
        g = np.minimum(g, n_n)
    return g


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64

    g = np.random.random((n, n)).astype(dtype)
    floyd(g, n)  # warm up

    g = np.random.random((n, n)).astype(dtype)
    tic = time.time()
    floyd(g, n)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
