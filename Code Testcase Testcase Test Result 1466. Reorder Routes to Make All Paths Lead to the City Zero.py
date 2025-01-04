#There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

#Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

#This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

#Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

#It's guaranteed that each city can reach city 0 after reorder.
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))

        reverse = 0
        visited = set()
        queue = [0]

        while queue:
            node = queue.pop()
            visited.add(node)

            for nd, st in graph[node]:
                if nd not in visited:
                    queue.append(nd)
                    if st:
                        reverse += 1
        return reverse

# in this problem, first add all the pair to the graph, the reverse is false
# at first, the queue only has 0, which means start from 0, visited add the node which already been poped from queue
# then search the new node and satute, if the node is not in visited, add it to the queue, if it's reverse, reverse + 1
