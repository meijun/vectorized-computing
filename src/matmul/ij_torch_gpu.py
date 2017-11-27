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

    a = torch.zeros(n, n).type(dtype).cuda()
    b = torch.rand(n, n).type(dtype).cuda()
    c = torch.rand(n, n).type(dtype).cuda()
    matmul(a, b, c, n, n)  # warm up
    torch.cuda.synchronize()

    a = torch.zeros(n, n).type(dtype).cuda()
    b = torch.rand(n, n).type(dtype).cuda()
    c = torch.rand(n, n).type(dtype).cuda()
    tic = time.time()
    matmul(a, b, c, n, n)
    torch.cuda.synchronize()
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
