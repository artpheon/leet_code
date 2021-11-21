class Solution(object):
    def edgesToGraph(edges):
        graph = {}
        for row in edges:
            if row[0] not in graph:
                graph[row[0]] = []
            if len(row) == 2:
                graph[row[0]].append(row[1])
                if row[1] not in graph:
                    graph[row[1]] = []
                graph[row[1]].append(row[0])
        return graph

    def hasPath(graph, A, B):
        que = [ A ]
        visited = []
        while que:
            current = que.pop(0)
            if current == B:
                return True
            visited.append(current)
            for node in graph[current]:
                if node not in visited:
                    que.append(node)
        return False


if __name__ == '__main__':
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('k', 'j'),
        ('o', 'n')
    ]
    graph = Solution.edgesToGraph(edges)
    print("Graph:")
    for key in graph.keys():
        print("{}: {}".format(key, graph[key]))
    print("Result:")
    print("There is path from I to M: {}".format(Solution.hasPath(graph, 'i', 'm')))
    print("There is path from L to J: {}".format(Solution.hasPath(graph, 'l', 'j')))
    print("There is path from K to O: {}".format(Solution.hasPath(graph, 'k', 'o')))
    print("There is path from N to O: {}".format(Solution.hasPath(graph, 'n', 'o')))
    print("There is path from O to I: {}".format(Solution.hasPath(graph, 'o', 'i')))
    print("There is path from K to K: {}".format(Solution.hasPath(graph, 'k', 'k')))
    print("There is path from K to J: {}".format(Solution.hasPath(graph, 'k', 'j')))
