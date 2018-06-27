package main

import (
	"fmt"
)

func fibb(x int) int {
	m := make(map[int]int)
	m[1], m[2] = 1, 1
	if x == 1 {
		return m[1]
	} else if x == 2 {
		return m[2]
	} else {
		m[x] = (fibb(x-1) + fibb(x-2))
		return m[x]
	}

}

func main() {
	fmt.Println(fibb(20))
}
