package singlenumbers

// Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
// You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
func SingleNumber(nums []int) []int {
	lookup := map[int]int{}
	for _, num := range nums {
		_, exists := lookup[num]
		if exists {
			lookup[num] += 1
		} else {
			lookup[num] = 1
		}
	}

	unique := []int{}

	for num, value := range lookup {
		if value == 1 {
			unique = append(unique, num)
		}
	}

	return unique
}
