package main

import "fmt"

func fibbWithMemo(x int) int {
	m := make(map[int]int)
	m[1], m[2] = 1, 1
	if x == 1 {
		return m[1]
	} else if x == 2 {
		return m[2]
	} else {
		m[x] = (fibbWithMemo(x-1) + fibbWithMemo(x-2))
		return m[x]
	}
}

func fasterFibb(x int) {
	a := []int{1, 1}
	for i := 2; i < x; i++ {
		a = append(a, (a[i-1] + a[i-2]))
	}
	fmt.Println(a)
}

func main() {
	//fmt.Println(fibbWithMemo(20))
	fasterFibb(20)
}
