#
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# There are multiple ways of solving this problem
# I have used the Quicksort method of solving
# 
# Due to shuffling of inputs and using Quick select method
# Time Complexity: O(N)

# Does inplace swapping of values
# The iterative method doesn't also use recursion stack
# Space Complexity: O(1)
#
# If using recursion
# every recursion call needs to maintain a stack - the no of times recursion is called
# Space Complexity: O(N)


from typing import List
from random import shuffle


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #
        # randomize the input array - which improves performance
        # in case of Quicksort
        #
        shuffle(nums)
        return self.kselect(nums, 0, len(nums) - 1, k)

    def kselect(self, arr, left, right, k):
        ki = len(arr) - k
        if left < right:
            pi = self.partition(arr, left, right)
            if ki < pi:
                self.kselect(arr, left, pi - 1, k)
            if ki > pi:
                self.kselect(arr, pi + 1, right, k)
        return arr[ki]

    def partition(self, arr, left, right):
        #
        # there are multiple ways of doing the partition
        # in this on we: select the last value as the pivot
        # we use two loop invariants: 
        # pi - represents lower bound index
        # ci - comprator to compare values in the array with pivot
        #
        pi = left - 1
        if left < right:
            pivot = arr[right]
            for ci in range(left, right):
                if arr[ci] <= pivot:
                    pi += 1
                    arr[pi], arr[ci] = arr[ci], arr[pi]
            #
            # swap the pivot value in its rightful place
            #
            arr[pi + 1], arr[right] = arr[right], arr[pi + 1]
        return pi + 1

    def kselect_iterative(self, arr, left, right, k):
        #
        # an iterative solution to reduct call back memory foot print
        #

        ki = len(arr) - k
        while left < right:
            pi = self.partition(arr, left, right)
            if ki < pi:
                right = pi - 1
            if ki > pi:
                left = pi + 1
            if ki == pi:
                break
        return arr[ki]


if __name__ == '__main__':
    items = [3, 2, 1, 5, 6, 4]
    k = 2
    ans = Solution().findKthLargest(items, k)
    print(ans)
