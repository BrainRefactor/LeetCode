#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
#

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binary_search_iterative(nums, 0, len(nums) - 1, target, True)
        last = self.binary_search_iterative(nums, 0, len(nums) - 1, target, False)

        # first = self.binary_search(nums, 0, len(nums) - 1, target, True)
        # last = self.binary_search(nums, 0, len(nums) - 1, target, False)

        return [first, last]

    #
    # because we know that inputs are sorted - we can take advantage of that
    #

    def binary_search(self, arr, low, high, target, is_first):
        #
        # base case test to make sure we dont go out of bound of given array
        #

        if high < low:
            return -1

        #
        # this formula for calculating `mid` makes sure that for large values of int there is no
        # overflow
        # especially in languages like Java/C/C++
        #

        mid = low + (high - low) // 2

        if is_first:
            if arr[mid] == target:
                if arr[mid - 1] < target or mid == 0:
                    return mid
                return self.binary_search(arr, low, mid - 1, target, is_first)
            if arr[mid] < target:
                return self.binary_search(arr, mid + 1, high, target, is_first)
            if arr[mid] > target:
                return self.binary_search(arr, low, mid - 1, target, is_first)
        else:
            if arr[mid] == target:
                if mid + 1 == len(arr):
                    return mid
                if arr[mid + 1] > target or mid == len(arr) - 1:
                    return mid
                return self.binary_search(arr, mid + 1, high, target, is_first)
            if arr[mid] < target:
                return self.binary_search(arr, mid + 1, high, target, is_first)
            if arr[mid] > target:
                return self.binary_search(arr, low, mid - 1, target, is_first)

    @staticmethod
    def binary_search_iterative(arr, low, high, target, is_first):
        while True:
            if high < low:
                return -1

            mid = low + (high - low) // 2

            if is_first:
                if arr[mid] == target:
                    if arr[mid - 1] < target or mid == 0:
                        return mid
                    else:
                        high = mid - 1
                if arr[mid] < target:
                    low = mid + 1
                if arr[mid] > target:
                    high = mid - 1
            else:
                if arr[mid] == target:
                    if mid == len(arr) - 1:
                        return mid
                    if arr[mid + 1] > target or mid == len(arr) - 1:
                        return mid
                    else:
                        low = mid + 1
                if arr[mid] < target:
                    low = mid + 1
                if arr[mid] > target:
                    high = mid - 1


if __name__ == '__main__':
    items_1 = [2, 2]
    x = 2

    ans = Solution().searchRange(items_1, x)
    print(ans)

    items_2 = [1, 2, 3, 4, 5, 6, 6, 7, 8]
    x = 6

    ans = Solution().searchRange(items_2, x)
    print(ans)
