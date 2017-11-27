import numpy as np


def matmul(a, b, c, m, n):
    for i in range(m):
        for j in range(n):
            a[i, j] = np.sum(b[i, :] * c[:, j])


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64

    a = np.zeros((n, n), dtype=dtype)
    b = np.random.random((n, n)).astype(dtype)
    c = np.random.random((n, n)).astype(dtype)
    matmul(a, b, c, n, n)  # warm up

    a = np.zeros((n, n), dtype=dtype)
    b = np.random.random((n, n)).astype(dtype)
    c = np.random.random((n, n)).astype(dtype)
    tic = time.time()
    matmul(a, b, c, n, n)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
