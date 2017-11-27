import tensorflow as tf
import numpy as np


def matmul(b, c):
    return tf.matmul(b, c)


def main():
    import sys
    import time

    n = int(sys.argv[1])
    dtype = np.float64
    with tf.device('/cpu:0'):
        bp = tf.placeholder(dtype=dtype, shape=[n, n])
        cp = tf.placeholder(dtype=dtype, shape=[n, n])
        a = matmul(bp, cp)
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
