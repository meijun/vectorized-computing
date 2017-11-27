import torch


def floyd(g, n):
    for k in range(n):
        n_n = g[:, k].contiguous().view(n, 1) + g[k, :].view(1, n)
        g = torch.min(g, n_n)
    return g


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = torch.DoubleTensor

    g = torch.rand((n, n)).type(dtype).cuda()
    floyd(g, n)  # warm up
    torch.cuda.synchronize()

    g = torch.rand((n, n)).type(dtype).cuda()
    torch.cuda.synchronize()
    tic = time.time()
    floyd(g, n)
    torch.cuda.synchronize()
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
