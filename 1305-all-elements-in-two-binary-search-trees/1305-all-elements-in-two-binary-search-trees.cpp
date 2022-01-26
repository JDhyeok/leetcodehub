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
// class Solution {
// public:
//     priority_queue<int, vector<int>, greater<int>> pq;
//     vector<int> answer;
    
//     void addElement(TreeNode* root){
//         if(root == NULL)
//             return;
//         addElement(root->left);
//         pq.push(root->val);
//         addElement(root->right);
//     }
    
//     vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
//         addElement(root1);
//         addElement(root2);

//         while(!pq.empty()){
//             answer.push_back(pq.top());
//             pq.pop();
//         }
//         return answer;
//     }
// };
class Solution {
public:
    vector<int> answer;
    
    void addElement(TreeNode* root){
        if(root == NULL)
            return;
        addElement(root->left);
        answer.push_back(root->val);
        addElement(root->right);
    }
    
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        addElement(root1);
        addElement(root2);

        sort(answer.begin(), answer.end());
        return answer;
    }
};
