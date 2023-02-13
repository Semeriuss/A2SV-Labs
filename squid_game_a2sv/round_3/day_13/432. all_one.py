from collections import defaultdict
import heapq


class AllOne:
    # O(1) time and O(N) space

    def __init__(self):
        self.store = defaultdict(int)
        self.minHeap = []
        self.maxHeap = []

    def inc(self, key: str) -> None:
        self.store[key] += 1

        heapq.heappush(self.minHeap, (self.store[key], key))
        heapq.heappush(self.maxHeap, (-self.store[key], key))

    def dec(self, key: str) -> None:
        self.store[key] -= 1
        if not self.store[key]:
            del self.store[key]

    def getMaxKey(self) -> str:

        while self.maxHeap:
            count, key = self.maxHeap[0]
            if -count == self.store[key]:
                return key
            else:
                heapq.heappop(self.maxHeap)
        return ""

    def getMinKey(self) -> str:

        while self.minHeap:
            count, key = self.minHeap[0]
            if count == self.store[key]:
                return key
            else:
                heapq.heappop(self.minHeap)
        return ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
