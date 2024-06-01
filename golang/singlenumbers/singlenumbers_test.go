package singlenumbers

import (
	"reflect"
	"testing"
)

func TestSuite(t *testing.T) {
	example_one_nums := []int{1, 2, 1, 3, 2, 5}
	example_one_expected := []int{3, 5}
	example_two_nums := []int{-1, 0}
	example_two_expected := []int{-1, 0}
	example_three_nums := []int{0, 1}
	example_three_expected := []int{0, 1}

	example_one_result := SingleNumber(example_one_nums)
	if !reflect.DeepEqual(example_one_result, example_one_expected) {
		t.Fatalf("Failed test one")
	}

	example_two_result := SingleNumber(example_two_nums)
	if !reflect.DeepEqual(example_two_result, example_two_expected) {
		t.Fatalf("Failed test two")
	}

	example_three_result := SingleNumber(example_three_nums)
	if !reflect.DeepEqual(example_three_result, example_three_expected) {
		t.Fatalf("Failed test three")
	}
}
