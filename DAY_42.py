# -----------------------------------------
# problem-1

# def kReverse(head, k):
#     # Write your code here
#     # Return the head of the updated linked list.
#     if not head or not head.next:
#         return head
#     dummy = Node(0)
#     dummy.next = head
#     pre = dummy
#     curr = None
#     nex = None
#     length = 0
#     temp = head
#     while temp:
#         length += 1
#         temp =temp.next
#     while length >= k:
#         curr = pre.next
#         nex = curr.next
#         for i in range(1,k):
#             curr.next = nex.next
#             nex.next = pre.next
#             pre.next = nex
#             nex =curr.next
#         prev = curr
#         length -=1 
#     return dummy.next

# -----------------------------------------
# problem-2

# class Node:
#     def __init__(self, val, next=None):
#         self.data = val
#         self.next = next


# def rotate(head: Node, k: int) -> Node:
#     # Write your code here.
    
#     temp = head
#     n = 0
#     while temp:
#         n += 1
#         temp = temp.next
#     dummy = Node(0)
#     temp = dummy
#     k = k % n
#     if not head or not head.next or k == 0:
#         return head
#     for i in range(n-k):
#         temp.next = head
#         head = head.next
#         temp = temp.next
#     temp.next = None
#     temp2 = head
#     while temp2.next:
#         temp2= temp2.next
#     temp2.next = dummy.next
#     return head

# ----------------------------------------------
# problem-3

# def flattenLinkedList(root: Node) -> Node:
#     def mergeTwoLists(a, b):
#         temp = Node(0)
#         res = temp
#         while a != None and b != None:
#             if a.data < b.data:
#                 temp.child = a
#                 temp = temp.child
#                 a = a.child
#             else:
#                 temp.child = b
#                 temp = temp.child
#                 b = b.child
#         if a:
#             temp.child = a
#         else:
#             temp.child = b
#         return res.child
#     if root == None or root.next == None:
#         return root
#     # recur for list on right
#     root.next = flattenLinkedList(root.next)


#     # now merge
#     root = mergeTwoLists(root, root.next)


#     # return the root
#     # it will be in turn merged with its left
#     return root



