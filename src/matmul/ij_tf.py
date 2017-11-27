import tensorflow as tf
import numpy as np


def matmul(b, c, m, n):
    a = []
    for i in range(m):
        ai = []
        for j in range(n):
            aij = tf.reduce_sum(b[i, :] * c[:, j])
            ai.append(aij)
        ai = tf.stack(ai)
        a.append(ai)
    a = tf.stack(a)
    return a


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64
    with tf.device('/cpu:0'):
        bp = tf.placeholder(dtype=dtype, shape=[n, n])
        cp = tf.placeholder(dtype=dtype, shape=[n, n])
        a = matmul(bp, cp, n, n)
        sess = tf.Session()
        b = np.random.random((n, n)).astype(dtype)
        c = np.random.random((n, n)).astype(dtype)
        sess.run(a, feed_dict={bp: b, cp: c})  # warm up

        b = np.random.random((n, n)).astype(dtype)
        c = np.random.random((n, n)).astype(dtype)
        tic = time.time()
        sess.run(a, feed_dict={bp: b, cp: c})
        toc = time.time()

        print(toc - tic)


if __name__ == '__main__':
    main()
