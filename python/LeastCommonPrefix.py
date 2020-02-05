# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of
# strings.

# TLDR!


class Solution:
    def longestCommonPrefix(self, strs):
        prefix = []
        for string in zip(*strs):
            if len(set(string)) == 1:
                prefix.append(string[0])
            else:
                break

        return "".join(prefix)


def solution(array):
    prefix = []

    for string in zip(*array):
        if len(set(string)) == 1:
            prefix.append(string[0])
        else:
            break

    return "".join(prefix)


if __name__ == "__main__":
    strings = ["flower", "flow", "flight"]
    # strings = ["dog","racecar","car"]
    # strings = ["aca", "cba"]

    result = solution(strings)

    print(result)
