# -------------------------------------------
# problem-1

# class Node:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
# def constructDLL(arr: [int]) -> Node:
#     head = Node(arr[0])
#     prevN = head
#     for i in range(1,len(arr)):
#         temp = Node(arr[i])
#         prevN.next = temp
#         temp.prev = prevN
#         prevN = temp 
#     return head

# -------------------------------------------
# problem-2

# class Node:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.prev = prev
#         self.next = next
# def insertAtTail(head: Node, k: int) -> Node:
#     new = Node(k)
#     if not head:
#         head = new
#         return head
#     temp =head
#     while temp.next != None:
#         temp = temp.next
#     temp.next = new
#     new.prev = temp
#     return head

# ---------------------------------------------
# problem-3

# class Node:
#     def __init__(self, data=0, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
# def deleteLastNode(head: Node) -> Node:
#     if head is None:
#         return None
#     if head.next is None:
#         # If there's only one node in the list, set head to None to empty the list.
#         return None
#     else:
#         # Traverse the list to find the last node.
#         temp = head
#         while temp.next is not None:
#             temp = temp.next
#         # Remove the last node by updating the previous node's "next" pointer.
#         temp.prev.next = None
#         # Update the "prev" pointer of the last node to None.
#         temp.prev = None
#     return head

# -----------------------------------------------
# problem-4

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
# def reverseDLL(head):
#     # Write your code here
#     if not head:
#         return None
#     currentNode = head
#     prevNode = None
#     while currentNode != None:
#         nextNode = currentNode.next
#         currentNode.prev = nextNode
#         currentNode.next = prevNode
#         prevNode = currentNode
#         currentNode = nextNode
#     head = prevNode
#     return head