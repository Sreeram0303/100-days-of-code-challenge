# problem - 1

# from typing import List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def construct_tree(arr, end, index):
#     if index > end:
#         return None

#     root = Node(arr[index])
#     root.left = construct_tree(arr, end, index * 2 + 1)
#     root.right = construct_tree(arr, end, index * 2 + 2)
#     return root

# def createTree(arr):
#     end = len(arr) - 1
#     index = 0
#     root = construct_tree(arr, end, index)
#     return root

# problem - 2

# from os import *
# from sys import *
# from collections import *
# from math import *

# # Following is the Binary Tree node structure:
# class BinaryTreeNode :
#     def __init__(self, data) :
#         self.data = data
#         self.left = None
#         self.right = None
# def inorder(node,ans):
#     if node == None:
#         return
#     inorder(node.left,ans)
#     ans.append(node.data)
#     inorder(node.right,ans)
# def preorder(node,ans):
#     if node == None:
#         return
#     ans.append(node.data)
#     preorder(node.left,ans)
#     preorder(node.right,ans)
# def postorder(node,ans):
#     if node == None:
#         return
#     postorder(node.left,ans)
#     postorder(node.right,ans)
#     ans.append(node.data)
# def getTreeTraversal(root):
#     ans = [[] for _ in range(3)]

#     inorder(root, ans[0])
#     preorder(root, ans[1])
#     postorder(root, ans[2])

#     return ans
