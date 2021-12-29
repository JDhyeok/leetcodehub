/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> answer = new ArrayList();
    
    public void inorder(TreeNode node){
        if(node == null)
            return;
        inorder(node.left);
        answer.add(node.val);
        inorder(node.right);
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        inorder(root);
        return answer;
    }
}