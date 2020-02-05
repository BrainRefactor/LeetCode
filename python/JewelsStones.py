# https://leetcode.com/problems/jewels-and-stones

# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many
# of the stones you have are also jewels.

# TLDR;


from collections import Counter


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        stones_count = Counter([k for k in S])

        for jem in J:
            if jem in stones_count:
                count += stones_count[jem]

        return count


def num_jewels_in_stones_better(J, S):
    """
    We know J is unique items list - this implementation is faster
    :param J: Jem
    :param S: Stones
    :return: int count
    """
    count = 0
    for jem in J:
        count += S.count(jem)

    return count


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"

    result = num_jewels_in_stones_better(J, S)

    print(result)
