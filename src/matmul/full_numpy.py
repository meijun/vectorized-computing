import numpy as np


def matmul(b, c, m, n, r):
    m_r_n = b.reshape(m, r, 1) * c.reshape(1, r, n)
    a = np.sum(m_r_n, axis=1)
    return a


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64

    b = np.random.random((n, n)).astype(dtype)
    c = np.random.random((n, n)).astype(dtype)
    matmul(b, c, n, n, n)  # warm up

    b = np.random.random((n, n)).astype(dtype)
    c = np.random.random((n, n)).astype(dtype)
    tic = time.time()
    matmul(b, c, n, n, n)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
