class Solution:
    @staticmethod
    def sortColors(arr):
        lower_idx = -1
        upper_idx = len(arr)
        c = 0
        while c < upper_idx:
            if arr[c] == 2:
                upper_idx -= 1
                arr[c], arr[upper_idx] = arr[upper_idx], arr[c]
            elif arr[c] == 0:
                lower_idx += 1
                arr[c], arr[lower_idx] = arr[lower_idx], arr[c]
                c += 1
            else:
                c += 1

        return arr


if __name__ == '__main__':
    items = [2, 0, 2, 1, 1, 0]
    ans = Solution().sortColors(items)
    print(ans)
