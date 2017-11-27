import torch


def matmul(a, b, c, m, n):
    for i in range(m):
        for j in range(n):
            a[i, j] = torch.sum(b[i, :] * c[:, j])


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = torch.DoubleTensor

    a = torch.zeros(n, n).type(dtype)
    b = torch.rand(n, n).type(dtype)
    c = torch.rand(n, n).type(dtype)
    matmul(a, b, c, n, n)  # warm up

    a = torch.zeros(n, n).type(dtype)
    b = torch.rand(n, n).type(dtype)
    c = torch.rand(n, n).type(dtype)
    tic = time.time()
    matmul(a, b, c, n, n)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
