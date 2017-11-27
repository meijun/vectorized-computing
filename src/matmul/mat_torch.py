import torch


def matmul(b, c):
    return torch.matmul(b, c)


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = torch.DoubleTensor

    b = torch.rand(n, n).type(dtype)
    c = torch.rand(n, n).type(dtype)
    matmul(b, c)  # warm up

    b = torch.rand(n, n).type(dtype)
    c = torch.rand(n, n).type(dtype)
    tic = time.time()
    matmul(b, c)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
