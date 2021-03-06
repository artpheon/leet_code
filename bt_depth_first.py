class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depthFirst(root: TreeNode) -> list[int]:
        result = []
        parents = [root,]

        while (parents):
            result.append(parents[0].val)
            if parents[0].left:
                parents.append(parents[0].left)
            if parents[0].right:
                parents.append(parents[0].right)
            parents.pop(0)
        return result



root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)
n6 = TreeNode(7)

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n5.left = n6

result = Solution.depthFirst(root)

for i in result:
    print(i, end=' ')
print()