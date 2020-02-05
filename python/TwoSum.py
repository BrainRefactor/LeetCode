# https://leetcode.com/problems/two-sum/

# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.

# TLDR!


class Solution:
    """
    Actual code that used for leetcode submission
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            other_number = target - nums[i]
            if other_number in hash_table:
                return [hash_table[other_number], i]
            hash_table[nums[i]] = i


def two_sum(nums, target):
    """
    Make use of Hashmap (dictionary)
    I iterate over the items and calculate the difference if I have come
    across a difference
    then that difference's index and my current is the pair
    otherwise I just store the value and its corresponding values
    I check for the difference condition first before adding as it ll handle
    duplicate values
    :param nums: List for numbers
    :param target: Two Sum
    :return: List of indexes
    """
    value_to_index = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in value_to_index:
            return [value_to_index[difference], i]
        value_to_index[nums[i]] = i


def two_sum_sorted(numbers, target):
    """
    Condition is input numbers is in sorted order
    :param numbers: List for numbers
    :param target: Two Sum
    :return: List of indexes
    """
    start = 0
    end = len(numbers) - 1

    while start != end:
        if numbers[start] + numbers[end] == target:
            return [start + 1, end + 1]  # index starting from 1 for solution
        elif numbers[start] + numbers[end] > target:
            end -= 1
        else:
            start += 1


if __name__ == "__main__":
    items = [2, 7, 11, 15]
    result = two_sum_sorted(items, 9)
    print(result)
