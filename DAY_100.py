# def pre_order_traversal(root):
#     pre_order = []
#     if not root:
#         return pre_order

#     stack = [root]

#     while stack:
#         top_node = stack.pop()
#         pre_order.append(top_node.data)

#         if top_node.right:
#             stack.append(top_node.right)
#         if top_node.left:
#             stack.append(top_node.left)

#     return pre_order



# def in_order_traversal(root):
#     in_order = []
#     stack = []

#     while True:
#         if root:
#             stack.append(root)
#             root = root.left
#         else:
#             if not stack:
#                 break
#             root = stack.pop()
#             in_order.append(root.data)
#             root = root.right

#     return in_order