package main

import (
	"os"
	"strconv"
	"math/rand"
	"time"
	"fmt"
)

type float = float64
var randFloat = rand.Float64

func matmul(a, b, c [][]float, m, n, r int) {
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < r; k++ {
				a[i][j] += b[i][k] * c[k][j]
			}
		}
	}
}

func rand2d(m, n int) [][]float {
	a := make([][]float, m)
	for i := 0; i < n; i++ {
		a[i] = make([]float, n)
		for j := 0; j < n; j++ {
			a[i][j] = randFloat()
		}
	}
	return a
}

func main() {
	n64, _ := strconv.ParseInt(os.Args[1], 10, 64)
	n := int(n64)
	a := make([][]float, n)
	for i := 0; i < n; i++ {
		a[i] = make([]float, n)
	}
	b := rand2d(n, n)
	c := rand2d(n, n)
	matmul(a, b, c, n, n, n)  // warm up

	a = make([][]float, n)
	for i := 0; i < n; i++ {
		a[i] = make([]float, n)
	}
	b = rand2d(n, n)
	c = rand2d(n, n)
	tic := time.Now()
	matmul(a, b, c, n, n, n)
	used := time.Since(tic)
	fmt.Println(used.Seconds())
}
