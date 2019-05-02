# -*- coding:utf-8 -*-


# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        d = 0
        children = [root]
        while len(children) > 0:
            grandchildren = []
            grandchildren += [child.left for child in children if child.left != None]
            grandchildren += [child.right for child in children if child.right != None]
            children = grandchildren
            d += 1
        return d
