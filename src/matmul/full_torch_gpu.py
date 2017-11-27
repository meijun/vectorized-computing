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

    b = torch.rand(n, n).type(dtype).cuda()
    c = torch.rand(n, n).type(dtype).cuda()
    matmul(b, c, n, n, n)  # warm up
    torch.cuda.synchronize()

    b = torch.rand(n, n).type(dtype).cuda()
    c = torch.rand(n, n).type(dtype).cuda()
    tic = time.time()
    matmul(b, c, n, n, n)
    torch.cuda.synchronize()
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
