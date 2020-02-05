# 
# 
# https://leetcode.com/problems/permutations/
# 
# Time Complexity : O(n!)


class Solution():
    res = []

    def permute(self, arr):
        self.res = []
        self.permute_helper(0, arr)
        return self.res

    @staticmethod
    def swap(i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

    def permute_helper(self, start, arr):
        if start == len(arr) - 1:
            self.res.append(arr[:])

        for i in range(start, len(arr)):
            self.swap(start, i, arr)
            self.permute_helper(start + 1, arr)
            #
            # we reset the array to its original state again
            # after the func is done - backtracking
            #
            self.swap(start, i, arr)


if __name__ == '__main__':
    nums = [1]
    ans = Solution().permute(nums)
    print(ans)
