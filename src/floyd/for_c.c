#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#define dtype double

void floyd(dtype **g, int n) {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dtype s = g[i][k] + g[k][j];
                if (g[i][j] > s) {
                    g[i][j] = s;
                }
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
    dtype **g = rand2d(n, n);
    floyd(g, n);  // warm up

    g = rand2d(n, n);
    struct timespec tic, toc;
    clock_gettime(CLOCK_REALTIME, &tic);
    floyd(g, n);
    clock_gettime(CLOCK_REALTIME, &toc);

    double used = (toc.tv_sec - tic.tv_sec) + (toc.tv_nsec - tic.tv_nsec) / 1e9;
    printf("%.9f\n", used);

    return 0;
}
