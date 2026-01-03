from math import inf
from heapq import heappop, heappush


class Solution:
    example = tuple[list[list[int]], int, int, int]
    example_1: example = ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2)
    example_2: example = ([[1, 2, 1]], 2, 1, 1)
    example_3: example = ([[1, 2, 1]], 2, 2, -1)
    examples: tuple[example, example, example] = (example_1, example_2, example_3)

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Find minimum time for signal to reach all nodes using Dijkstra's algorithm.
        """

        graph: dict[int, list[tuple[int, int]]] = {}
        q: list[tuple[int | float, int]] = []
        signal_times: dict[int, int | float] = {}

        # Build adjacency list: node -> [(neighbor, travel_time), ...]
        for node in range(1, n + 1):
            graph[node] = []
        for source_node, destination_node, edge_time in times:
            graph[source_node].append((destination_node, edge_time))

        # Initialize all nodes to infinity, except start node k (set to 0)
        for node in range(1, n + 1):
            signal_times[node] = inf if node != k else 0

        # Push first node onto the heap in format (time, node)
        heappush(q, (signal_times[k], k))

        # Process all nodes using Dijkstra's algorithm
        while q:
            current_time, node = heappop(q)

            # Skip if we already found a better path to this node
            if current_time > signal_times[node]:
                continue

            neighbors = graph[node]

            # Relax edges: update neighbor times if we found a shorter path
            for destination_node, edge_time in neighbors:
                new_time = current_time + edge_time
                if new_time >= signal_times[destination_node]:
                    continue
                else:
                    signal_times[destination_node] = new_time
                    heappush(q, (new_time, destination_node))

        # Return max time (last node reached), or -1 if any node unreachable
        longest_time: int | float = max(signal_times.values())
        return int(longest_time) if longest_time != inf else -1

    def test(self) -> None:
        for test_case in self.examples:
            assert self.networkDelayTime(test_case[0], test_case[1], test_case[2]) == test_case[3]


if __name__ == "__main__":
    solution = Solution()
    solution.test()
