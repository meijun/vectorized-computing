import torch


def matmul(b, c):
    return torch.matmul(b, c)


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = torch.DoubleTensor

    b = torch.rand(n, n).type(dtype).cuda()
    c = torch.rand(n, n).type(dtype).cuda()
    matmul(b, c)  # warm up
    torch.cuda.synchronize()

    b = torch.rand(n, n).type(dtype).cuda()
    c = torch.rand(n, n).type(dtype).cuda()
    tic = time.time()
    matmul(b, c)
    torch.cuda.synchronize()
    toc = time.time()

    print(toc - tic)


if __name__ == '__main__':
    main()
