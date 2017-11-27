
def floyd(g, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])


def main():
    import sys
    import time
    import random

    n = int(sys.argv[1])

    g = [[random.random() for _ in range(n)] for _ in range(n)]
    floyd(g, n)  # warm up

    g = [[random.random() for _ in range(n)] for _ in range(n)]
    tic = time.time()
    floyd(g, n)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
