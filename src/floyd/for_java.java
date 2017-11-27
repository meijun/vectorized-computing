public class for_java {
    private static void floyd(double[][] g, int n) {
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    g[i][j] = Math.min(g[i][j], g[i][k] + g[k][j]);
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
        double[][] g = rand2d(n, n);
        floyd(g, n);  // warm up

        g = rand2d(n, n);
        long tic = System.nanoTime();
        floyd(g, n);
        long toc = System.nanoTime();
        System.out.println((toc - tic) / 1e9);
    }
}
