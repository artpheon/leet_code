class Graph(dict):
    def __str__(self):
        iterator = iter(self)
        key = next(iterator, None)
        string = ""
        while key:
            string = string + "{}: {}".format(key, self[key])
            key = next(iterator, None)
            string = string if not key else string + "\n"
        return string

def edges_to_graph(edges):
    graph = Graph()
    for edge in edges:
        if edge[0] not in graph.keys():
            graph[edge[0]] = []
        if len(edge) == 2:
            if edge[1] not in graph.keys():
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
    return graph

def components_count(graph):
    count = 0
    visited = []
    stack = []
    for key in graph.keys():
        if key not in visited:
            #checking every key if not checked yet
            count = count + 1
            stack.append(key)
            while stack:
                current = stack.pop()
                visited.append(current)
                for val in graph[current]:
                    if val not in visited:
                        stack.append(val)
    return count

def test_graph():
    edges = [
        (1, 2),
        (3, ),
        (5, 6),
        (4, 6),
        (8, 6),
        (7, 6)
    ]
    graph = edges_to_graph(edges)
    components = components_count(graph)
    print("Graph:\n{}\nIt has {} components".format(graph, components))

if __name__ == '__main__':
    test_graph()