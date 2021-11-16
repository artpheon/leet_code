class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(root: TreeNode) -> list[int]:
        result = []
        st = [root,]
        while st:
            root = st.pop()
            result.append(root.val)
            if root.right:
                st.append(root.right)
            if root.left:
                st.append(root.left)
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

res = Solution.preorderTraversal(root)
print('Traversed:')
for x in res:
    print(x, end=' ')
print()