class Solution(object):
    def hasPath_depth(graph, a, z) -> bool:
        stack = [ a ]
        while stack:
            current = stack.pop()
            if current == z:
                return True
            for key in graph[current]:
                stack.append(key)
        return False
    
    def hasPath_breadth(graph, a, z):
        que = [ a ]
        while que:
            current = que.pop(0)
            if current == z:
                return True
            for key in graph[current]:
                que.append(key)
        return False


if __name__ == '__main__':
    graph = {
        'f': ['i', 'g'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': [],
    }

    print("Has path from J to H: {}".format(Solution.hasPath_depth(graph, 'j', 'h')))
    print("Has path from G to K: {}".format(Solution.hasPath_depth(graph, 'g', 'k')))
    print("Has path from F to K: {}".format(Solution.hasPath_depth(graph, 'f', 'k')))
    print("Has path from F to J: {}".format(Solution.hasPath_depth(graph, 'f', 'j')))

    print("Has path from J to H: {}".format(Solution.hasPath_breadth(graph, 'j', 'h')))
    print("Has path from G to K: {}".format(Solution.hasPath_breadth(graph, 'g', 'k')))
    print("Has path from F to K: {}".format(Solution.hasPath_breadth(graph, 'f', 'k')))
    print("Has path from F to J: {}".format(Solution.hasPath_breadth(graph, 'f', 'j')))