#include <vector>
#include <stack>
#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    static std::vector<int> preorderTraversal(TreeNode* root) {
        std::stack<TreeNode*> st;
        TreeNode* check = nullptr;
        std::vector<int> result;

        if (root)
            st.push(root);
        while (!st.empty()) {
            check = st.top();
            st.pop();
            result.push_back(check->val);
            if (check->right)
                st.push(check->right);
            if (check->left)
                st.push(check->left);
        }
        return result;
    }
};

int main() {
    TreeNode root = TreeNode(1);
    TreeNode n1 = TreeNode(2);
    TreeNode n2 = TreeNode(3);
    TreeNode n3 = TreeNode(4);
    TreeNode n4 = TreeNode(5);
    TreeNode n5 = TreeNode(6);
    TreeNode n6 = TreeNode(7);

    root.left = &n1;      //      1
    root.right = &n2;     //   2     3
    n1.left = &n3;        // 4  5   6
    n1.right = &n4;       //       7
    n2.left = &n5;
    n5.left = &n6;

    std::vector<int> traversed = Solution::preorderTraversal(&root);
    std::cout << "Traversed:\n";
    for (auto &x : traversed) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
}