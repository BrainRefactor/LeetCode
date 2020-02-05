#
# https://leetcode.com/problems/queue-reconstruction-by-height/
# 
# Time Complexity:
# Sorting: O(nlogn)
# 
# inserting to rightful place can be considered as O(n^2)
# 
# Space Complexity: O(n)
#


class Solution:
    @staticmethod
    def reconstruct(people):
        #
        # sort the people in decreasing order of their height
        # Time Complexity: O(nlogn)
        #
        people.sort(key=lambda x: (-x[0], x[1]))
        res = [[None, None] for _ in range(len(people))]
        ans = []

        #
        # insert the people based on thier k value - no of people standing in front
        # or visible to them
        #
        # Time Complexity: O(n^2)
        for item in people:
            ans.insert(item[1], item)
        return ans

    @staticmethod
    def insertion(arr, person, idx):
        #
        # a naive way to insert elements to a index
        #
        existing = arr[idx]
        if existing[0] is None and existing[1] is None:
            arr[idx] = person
        else:
            length = len(arr) - 1
            while length > idx:
                arr[length] = arr[length - 1]
                length -= 1
            arr[idx] = person


if __name__ == '__main__':
    items = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ans = Solution().reconstruct(items)
    print(ans)
