#
# https://leetcode.com/problems/maximum-subarray/
#
# Time Complexity:
# O(n)
#


class Solution():

    def max_sub_array(self, arr):

        max_sum = current_sum = arr[0]

        for i in range(1, len(arr)):
            current_sum += arr[i]
            if arr[i] > current_sum:
                current_sum = arr[i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum


def max_sub_array_brute_force(arr):
    """
    Brute force approact towards solving
    Time Complexity:
    O(n^2)
    """
    max_sum = float('-inf')

    for start in range(len(arr)):
        current_sum = 0
        for end in range(start, len(arr)):
            current_sum += arr[end]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


if __name__ == '__main__':
    items = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ans = Solution().max_sub_array(items)
    print(ans)
