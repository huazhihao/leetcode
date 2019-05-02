# -*- coding:utf-8 -*-


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        children = [root]
        while len(children) > 0:
            vals = []
            grandchildren = []
            for child in children:
                if child != None:
                    vals.append(child.val)
                    grandchildren.append(child.left)
                    grandchildren.append(child.right)
            if len(vals) == 0:
                break
            results.append(vals)
            children = grandchildren
        return results
