#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#define dtype double

void matmul(dtype **a, dtype **b, dtype **c, int m, int n, int r) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < r; k++) {
                a[i][j] += b[i][k] * c[k][j];
            }
        }
    }
}

dtype **rand2d(int m, int n) {
    dtype **a = (dtype **) malloc(m * sizeof(dtype *));
    for (int i = 0; i < m; i++) {
        a[i] = (dtype *) malloc(n * sizeof(dtype));
        for (int j = 0; j < n; j++) {
            a[i][j] = (dtype) rand() / (dtype) RAND_MAX + 1.0;
        }
    }
    return a;
}

int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    dtype **a = rand2d(n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            a[i][j] = 0.0;
        }
    }
    dtype **b = rand2d(n, n);
    dtype **c = rand2d(n, n);
    matmul(a, b, c, n, n, n);  // warm up

    a = rand2d(n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            a[i][j] = 0.0;
        }
    }
    b = rand2d(n, n);
    c = rand2d(n, n);
    struct timespec tic, toc;
    clock_gettime(CLOCK_REALTIME, &tic);
    matmul(a, b, c, n, n, n);
    clock_gettime(CLOCK_REALTIME, &toc);

    double used = (toc.tv_sec - tic.tv_sec) + (toc.tv_nsec - tic.tv_nsec) / 1e9;
    printf("%.9f\n", used);

    return 0;
}
