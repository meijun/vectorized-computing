public class for_java {
    private static void matmul(double[][] a, double[][] b, double[][] c, int m, int n, int r) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < r; k++) {
                    a[i][j] += b[i][k] * c[k][j];
                }
            }
        }
    }

    private static double[][] rand2d(int m, int n) {
        double[][] a = new double[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = Math.random();
            }
        }
        return a;
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        double[][] a = new double[n][n];
        double[][] b = rand2d(n, n);
        double[][] c = rand2d(n, n);
        matmul(a, b, c, n, n, n);  // warm up

        a = new double[n][n];
        b = rand2d(n, n);
        c = rand2d(n, n);
        long tic = System.nanoTime();
        matmul(a, b, c, n, n, n);
        long toc = System.nanoTime();
        System.out.println((toc - tic) / 1e9);
    }
}
