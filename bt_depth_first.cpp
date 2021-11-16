#include <vector>
#include <queue>
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
    static std::vector<int> depthFirst(TreeNode* root) {
        std::queue<TreeNode*> que;
        std::vector<int> result;
        std::size_t size = 0;

        if (root != nullptr) {
            que.push(root);
            while (!que.empty()) {
                result.push_back(que.front()->val);
                if (que.front()->left != nullptr)
                    que.push(que.front()->left);
                if (que.front()->right != nullptr)
                    que.push(que.front()->right);
                que.pop();
            }
        }
        return result;
            
    };

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

    std::vector<int> traversed = Solution::depthFirst(&root);
    std::cout << "Traversed:\n";
    for (auto &x : traversed) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
}