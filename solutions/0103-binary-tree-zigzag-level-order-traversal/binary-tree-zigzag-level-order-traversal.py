# -*- coding:utf-8 -*-


# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
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
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ll = []
        if root == None:
            return ll
        children = [root]
        r = False
        while len(children) > 0:
            l = []
            grandchildren = []
            
            for child in children:
                l.append(child.val)
                if child.left != None:
                    grandchildren.append(child.left)
                if child.right != None:
                    grandchildren.append(child.right)
            if r:
                l = l[::-1]
            children = grandchildren
            ll.append(l)
            r = not r

        return ll
            
