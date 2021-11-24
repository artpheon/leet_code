from graph.graph import Graph, get_graph_by_edges

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
    g = get_graph_by_edges(edges)
    components = components_count(g)
    print("Graph:\n{}\nIt has {} components".format(g, components))

if __name__ == '__main__':
    test_graph()