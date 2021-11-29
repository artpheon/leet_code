from graph.graph import get_graph_by_edges

def shortestPath(g, A, B):
    visited = []
    que = [ (A, 0), ]
    while que:
        key, distance = que.pop(0)
        if key == B:
            return distance
        visited.append(key)
        print("current: {}".format(key))
        for node in g[key]:
            if node not in visited:
                que.append((node, distance + 1))
    return float('inf')

edges = [
    ('w', 'x'),
    ('x', 'y'),
    ('z', 'y'),
    ('z', 'v'),
    ('w', 'v'),
    ('a', 'b'),
]

g = get_graph_by_edges(edges)
result = shortestPath(g, 'a', 'a')
print("shortest path: {}".format(result))