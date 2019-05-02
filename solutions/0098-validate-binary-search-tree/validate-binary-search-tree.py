# -*- coding:utf-8 -*-


# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# 	The left subtree of a node contains only nodes with keys less than the node's key.
# 	The right subtree of a node contains only nodes with keys greater than the node's key.
# 	Both the left and right subtrees must also be binary search trees.
#
#
#  
#
# Example 1:
#
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        def _isValidBST(left, node, right):
            print(left, node.val, right)
            if node.left != None:
                if node.left.val >= node.val:
                    print("node.left.val >= node.val")
                    return False
                if left != None and node.left.val <= left:
                    print("left != None and node.left.val <= left")
                    return False
                if not _isValidBST(left, node.left, node.val):
                    return False
            if node.right != None:
                if node.right.val <= node.val:
                    print("node.right.val <= node.val")
                    return False
                if right != None and node.right.val >= right:
                    print("right != None and node.right.val >= right")
                    return False
                if not _isValidBST(node.val, node.right, right):
                    return False
            return True
        return _isValidBST(None, root, None)
        
