# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/
#
# Time Complexity: O(n)
#
# Space Complexity: O(26)


from collections import Counter

def is_anagram(a, b):
    if Counter(a) == Counter(b):
        return True
    return False


class Solution:
    @staticmethod
    def find_anagram_indices_brute_force(s, w):
        res = []

        if len(s) == 0 or s is None:
            return res

        for i in range(len(s) - len(w) + 1):
            window = s[i:i+len(w)]
            if is_anagram(w, window):
                res.append(i)
        return res

    @staticmethod
    def find_anagram_indices(s, w):
        res = []

        if len(s) == 0 or s is None:
            return res

        window_map = [0] * 30
        for c in w:
            offset = ord(c) - ord('a')
            window_map[offset] += 1

        left_index = 0
        right_index = 0
        count = len(w)

        while right_index < len(s):
            if window_map[ord(s[right_index]) - ord('a')] >= 1:
                count -= 1
            window_map[ord(s[right_index]) - ord('a')] -= 1
            right_index += 1

            if count == 0:
                res.append(left_index)

            if right_index - left_index == len(w):
                if window_map[ord(s[left_index]) - ord('a')] >= 0:
                    count += 1
                window_map[ord(s[left_index]) - ord('a')] += 1
                left_index += 1
        return res
