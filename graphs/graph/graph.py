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

def get_graph_by_edges(edges):
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

def _test():
    g = Graph({
        'key': 666,
    })
    assert g['key'] == 666

if __name__ == '__main__':
    _test()