package main

import (
	"os"
	"strconv"
	"math/rand"
	"time"
	"fmt"
	"math"
)

type float = float64
var randFloat = rand.Float64

func floyd(g [][]float, n int) {
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				g[i][j] = math.Min(g[i][j], g[i][k] + g[k][j])
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
	g := rand2d(n, n)
	floyd(g, n) // warm up

	g = rand2d(n, n)
	tic := time.Now()
	floyd(g, n)
	used := time.Since(tic)
	fmt.Println(used.Seconds())
}
