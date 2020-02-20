#
#
# https://leetcode.com/problems/find-median-from-data-stream/
#
# Time Complexity : O(nlogn) as we are doing heappush and heappop
# Space Complexity: O(n)
#
# for maintaining heap we are using python builtin heapq module
# which doesn't support max heap, so we use min heap and pass negative values
# to make it work like max heap

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def rebalance(self):
        if len(self.min_heap) > len(self.max_heap) + 1:
            root = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * root)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            root = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, root)
        else:
            pass

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            heapq.heappush(self.min_heap, num)
        else:
            current_median = self.findMedian()

            if num > current_median:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -1 * num)
        self.rebalance()

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            median = self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            median = -1 * self.max_heap[0]
        else:
            median = (self.min_heap[0] + (-1 * self.max_heap[0])) / 2.0
        return median
