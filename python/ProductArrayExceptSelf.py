# https://leetcode.com/problems/product-of-array-except-self/
#
# Time Complexity: O(n)
# Space Complexity: O(2n)


from typing import List

class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        if len(nums) == 0 or nums is None:
            return []

        prefix = []
        suffix = []

        for i in nums:
            if len(prefix) == 0:
                prefix.append(i)
            else:
                product = prefix[-1] * i
                prefix.append(product)

        for i in reversed(nums):
            if len(suffix) == 0:
                suffix.append(i)
            else:
                product = suffix[-1] * i
                suffix.append(product)

        suffix = [k for k in reversed(suffix)]

        results = []
        for i in range(len(nums)):
            if i == 0:
                results.append(suffix[i+1])
            elif i == len(nums) - 1:
                results.append(prefix[i-1])
            else:
                product = prefix[i-1] * suffix[i+1]
                results.append(product)

        return results
