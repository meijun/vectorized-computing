import torch


def matmul(b, c, m, n, r):
    m_r_n = b.view(m, r, 1) * c.view(1, r, n)
    a = torch.sum(m_r_n, dim=1)
    return a


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = torch.DoubleTensor

    b = torch.rand(n, n).type(dtype)
    c = torch.rand(n, n).type(dtype)
    matmul(b, c, n, n, n)  # warm up

    b = torch.rand(n, n).type(dtype)
    c = torch.rand(n, n).type(dtype)
    tic = time.time()
    matmul(b, c, n, n, n)
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
