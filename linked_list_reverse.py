class Node(object):
    def __init__(self, val: int = 0) -> None:
        super().__init__()
        self.val = val
        self.next: Node = None
    
    def printSelf(self):
        print("List:\n[{}]->[".format(self.val), end='')
        run = self.next
        while run:
            print('{}]-->['.format(run.val), end='')
            run = run.next
        print('None]')

class List(object):
    def __init__(self, root: Node) -> None:
        super().__init__()
        self.root = root
    
    def printList(self):
        self.root.printSelf()

    def pushNode(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            tmp = self.root
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(val)
        return self


class Solution(object):
    def reverseLinkedList(list: List):
        prev = None
        curr = list.root
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        list.root = prev

if __name__ == '__main__':
    root = Node(2)
    l = List(root)
    l.pushNode(4).pushNode(6).pushNode(8).pushNode(10)
    l.printList()
    Solution.reverseLinkedList(l)
    l.printList()
    Solution.reverseLinkedList(l)
    l.printList()

