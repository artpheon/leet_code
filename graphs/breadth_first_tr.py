class Traversal(object):
    def breadthFirst(graph, start):
        que = [ start ]
        result = [ ]
        while (que):
            current = que.pop(0)
            for key in current:
                result.append(key)
                que.append(graph[key])
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
    res = Traversal.breadthFirst(graph=graph, start='a')
    print(res)