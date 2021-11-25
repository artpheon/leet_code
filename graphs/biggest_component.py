from graph.graph import Graph, get_graph_by_edges

def biggest_component(graph):
    biggest = 0
    visited = []
    stack = []
    for key in graph.keys():
        if key not in visited:
            count = 0
            #checking every key if not checked yet
            stack.append(key)
            while stack:
                current = stack.pop()
                visited.append(current)
                for val in graph[current]:
                    if val not in visited:
                        count += 1
                        stack.append(val)
            biggest = count if count > biggest else biggest
    return biggest

if __name__ == '__main__':
    edges = [
        (0, 1),
        (0, 5),
        (0, 8),
        (5, 8),
        (4, 2),
        (4, 3),
        (3, 2),
        (3, 7),
        (90, 1),
        (20, 27),
        (20, 16),
        (20, 21),
        (20, 19),
        (19, 21)
    ]
    g = get_graph_by_edges(edges)
    biggest = biggest_component(g)
    print("Graph:")
    print(g)
    print("Biggest component: %d nodes" % biggest)