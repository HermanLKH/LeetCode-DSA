/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        
        deque<TreeNode*> q;
        q.push_back(root);

        int depth = 0;
        int size = 0;
        TreeNode* node;

        while (!q.empty()) {
            size = q.size();

            for (int i = 0; i < size; i++) {
                node = q.front();
                q.pop_front();

                if (node->left != nullptr) {
                    q.push_back(node->left);
                }

                if (node->right != nullptr) {
                    q.push_back(node->right);
                }
            }
            depth += 1;
        }

        return depth;
    }
};