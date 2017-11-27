import tensorflow as tf
import numpy as np


def floyd(g, n):
    for k in range(n):
        n_n = tf.reshape(g[:, k], [n, 1]) + tf.reshape(g[k, :], [1, n])
        g = tf.minimum(g, n_n)
    return g


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64
    with tf.device('/gpu:0'):
        gp = tf.placeholder(dtype=dtype, shape=[n, n])
        gr = floyd(gp, n)
        sess = tf.Session()

        g = np.random.random((n, n)).astype(dtype)
        sess.run(gr, feed_dict={gp: g})  # warm up

        g = np.random.random((n, n)).astype(dtype)
        tic = time.time()
        sess.run(gr, feed_dict={gp: g})
        toc = time.time()

        print(toc - tic)


if __name__ == '__main__':
    main()
