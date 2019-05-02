# -*- coding:utf-8 -*-


# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [3,2,1]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        if root == None:
            return output
        s = [root]
        while len(s) > 0:
            n = s.pop()
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
            output.append(n.val)
        return output[::-1]
