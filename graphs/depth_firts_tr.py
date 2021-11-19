class Traversal(object):
    def depthFirst(graph, start):
        result = []
        stack = [start]
        while stack:
            current = stack.pop()
            print(current, end=' ')
            result.append(current)
            stack = stack + [key for key in graph[current]]
        return result
    
    def depthFirst_recursive(graph: dict, start):
        result = [ start ]
        for i in graph[start]:
            result = result + Traversal.depthFirst_recursive(graph, i)
        return result


if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'c': ['e',],
        'b': ['d',],
        'd': ['f',],
        'e': [],
        'f': [],
    }
    res = Traversal.depthFirst_recursive(graph=graph, start='a')
    print(res)