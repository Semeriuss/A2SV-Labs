from collections import defaultdict, deque
from typing import List


class Solution:
    # O(N^2) time and space
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        visited_buses = set()
        visited_stops = set()
        que = deque([(source, 0)])
        while que:
            for _ in range(len(que)):
                curStop, steps = que.popleft()
                if curStop == target:
                    return steps

                for id in graph[curStop]:
                    if id not in visited_buses:
                        visited_buses.add(id)

                        for stop in routes[id]:
                            if stop not in visited_stops:
                                que.append((stop, steps + 1))
                                visited_stops.add(stop)

        return -1
