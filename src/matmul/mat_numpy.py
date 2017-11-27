import numpy as np


def matmul(b, c):
    return np.matmul(b, c)


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64

    b = np.random.random((n, n)).astype(dtype)
    c = np.random.random((n, n)).astype(dtype)
    matmul(b, c)  # warm up

    b = np.random.random((n, n)).astype(dtype)
    c = np.random.random((n, n)).astype(dtype)
    tic = time.time()
    matmul(b, c)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
