#
# https://leetcode.com/problems/ransom-note/
#
# We make use of builtin data structure callec Counter from the collections package
# We could have also used normal dictionary or default dict
#
# Time Complexity: O(n)

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not (Counter(ransomNote) - Counter(magazine)):
            return True
        return False


if __name__ == '__main__':
    magazine = 'ab'
    ransom = 'a'
    ans = Solution().canConstruct(ransom, magazine)
    print(ans)
