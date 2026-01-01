from math import inf


class Solution:
    def build_graph(self, times: list[list[int]], number_of_nodes: int) -> dict[int, dict[int, int]]:
        """Build adjacency list representation of the graph"""
        graph: dict[int, dict[int, int]] = {}

        # Initialize empty neighbors for each node
        for n in range(1, number_of_nodes + 1):
            graph[n] = {}

        # Add edges: graph[source][destination] = travel_time
        for entry in times:
            graph[entry[0]].update({entry[1]: entry[2]})

        return graph

    def find_shortest_signal(self, signal_times: dict[int, int | float], processed: set[int]) -> int | None:
        """Find the unprocessed node with the shortest signal time (Dijkstra's greedy step)"""
        shortest_signal = inf
        closest_node = None
        for item in signal_times.items():
            if item[1] < shortest_signal and item[0] not in processed:
                shortest_signal = item[1]
                closest_node = item[0]
        return closest_node

    def find_longest_signal(self, signal_times: dict[int, int | float]) -> int | float:
        """Find the maximum signal time across all nodes (time for all nodes to receive signal)"""
        longest_signal: int | float = 0

        for item in signal_times.values():
            if item > longest_signal:
                longest_signal = item

        # If any node is unreachable (still inf), return -1
        return longest_signal if longest_signal != inf else -1

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int | float:
        """Dijkstra's algorithm to find minimum time for signal to reach all nodes"""
        graph: dict[int, dict[int, int]] = self.build_graph(times, n)

        processed: set[int] = set()

        # Initialize all nodes to infinity except starting node k (set to 0)
        signal_times: dict[int, int | float] = {}
        for node in range(1, n + 1):
            signal_times[node] = inf if node != k else 0

        # Start from node k
        current_node: int | None = k

        # Process all nodes using Dijkstra's algorithm
        while current_node and len(processed) < n:
            neighbor_nodes = graph[current_node]
            current_time = signal_times[current_node]

            # Relaxation step: update neighbor times if we found a shorter path
            for nbr in neighbor_nodes.keys():
                new_time = current_time + neighbor_nodes[nbr]
                if new_time < signal_times[nbr]:
                    signal_times[nbr] = new_time

            processed.add(current_node)

            # Greedily select the next unprocessed node with shortest time
            current_node = self.find_shortest_signal(signal_times, processed)

        return self.find_longest_signal(signal_times)
