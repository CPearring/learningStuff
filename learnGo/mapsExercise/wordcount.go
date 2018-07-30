package main

import (
	"fmt"
	"strings"

	"golang.org/x/tour/wc"
)

// WordCount vscode is asking for a comment here?
// that's actually pretty cool
func WordCount(s string) map[string]int {
	fmt.Println(strings.Fields(s))
	c := strings.Fields(s)
	m := make(map[string]int)
	for _, value := range c {
		m[value]++
	}

	return m
}

func main() {
	wc.Test(WordCount)
}
