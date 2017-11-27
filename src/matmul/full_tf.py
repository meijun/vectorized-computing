import tensorflow as tf
import numpy as np


def matmul(b, c, m, n, r):
    m_r_n = tf.reshape(b, [m, r, 1]) * tf.reshape(c, [1, r, n])
    a = tf.reduce_sum(m_r_n, axis=1)
    return a


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64
    with tf.device('/cpu:0'):
        bp = tf.placeholder(dtype=dtype, shape=[n, n])
        cp = tf.placeholder(dtype=dtype, shape=[n, n])
        a = matmul(bp, cp, n, n, n)
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
