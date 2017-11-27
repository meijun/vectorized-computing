
def matmul(a, b, c, m, n, r):
    for i in range(m):
        for j in range(n):
            for k in range(r):
                a[i][j] += b[i][k] * c[k][j]


def main():
    import sys
    import time
    import random

    n = int(sys.argv[1])

    a = [[0.0 for _ in range(n)] for _ in range(n)]
    b = [[random.random() for _ in range(n)] for _ in range(n)]
    c = [[random.random() for _ in range(n)] for _ in range(n)]
    matmul(a, b, c, n, n, n)  # warm up

    a = [[0.0 for _ in range(n)] for _ in range(n)]
    b = [[random.random() for _ in range(n)] for _ in range(n)]
    c = [[random.random() for _ in range(n)] for _ in range(n)]
    tic = time.time()
    matmul(a, b, c, n, n, n)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
