# --------------------------------------
# problem-1

# def findIntersection(firstHead, secondHead):----------------optimal solution
	# Write your code here.
    # temp1 = firstHead
    # temp2 = secondHead
    # while temp1 != temp2:
    #     if temp1:
    #         temp1 = temp1.next
    #     else:
    #         temp1 = secondHead
    #     if temp2:
    #         temp2 = temp2.next
    #     else:
    #         temp2 = firstHead
    # return temp1
# -----------------------------------2nd approach
# def findIntersection(firstHead, secondHead):
#     def difinlen(head1,head2):
#         len1 = 0
#         len2 = 0
#         while head1 or head2:
#             if head1:
#                 len1 += 1
#                 head1 = head1.next
#             if head2:
#                 len2 += 1
#                 head2 = head2.next
#         return (len1-len2)
#     diff = difinlen(firstHead,secondHead)
#     temp1 = firstHead
#     temp2 = secondHead
#     if diff > 0:
#         while diff:
#             temp1 = temp1.next
#             diff -= 1
#     else:
#         while diff:
#             temp2 = temp2.next
#             diff += 1
#     while temp1:
#         if temp1 == temp2:
#             return temp1
#         temp1 = temp1.next
#         temp2 = temp2.next
#     return temp1

# ----------------------------------------
# problee-2

# def addOne(head: Node) -> Node:
# def reverse_ll(head):
#     if not head or not head.next:
#         return head

#     prev, curr, nxt = None, head, head.next
#     while curr and curr.next:
#         curr.next = prev
#         prev = curr
#         curr = nxt
#         nxt = nxt.next
#     curr.next = prev
#     return curr
#     # write your code here
#     new_head = reverse_ll(head)

#     temp = new_head
#     carry = 0
#     while temp:
#         if temp.data < 9:
#             temp.data += 1
#             carry = 0
#             break
#         else:
#             temp.data = 0
#             carry = 1
#         temp = temp.next

#     head = reverse_ll(new_head)
#     if carry == 1:
#         nn = Node(1)
#         nn.next = head
#         head = nn
#     return head

# ------------------------------------------------
# problem-3

# def addTwoNumbers(l1: Node, l2: Node) -> Node:
#         dummy = Node()
#         temp = dummy
#         carry = 0
#         while (l1 != None or l2 != None) or carry:
#             sum = 0
#             if l1 != None:
#                 sum += l1.data
#                 l1 = l1.next
#             if l2 != None:
#                 sum += l2.data
#                 l2 = l2.next
#             sum += carry
#             carry = sum // 10
#             node = Node(sum % 10)
#             temp.next = node
#             temp = temp.next
#         return dummy.next

# ----------------------------------------------------
# problem-4

# def sortList(head):
#     temp = head
#     zcnt = 0
#     ocnt = 0
#     tcnt = 0
#     while temp:
#         if temp.data == 0:
#             zcnt += 1
#         elif temp.data == 1:
#             ocnt += 1
#         else:
#             tcnt += 1
#         temp = temp.next
#     temp = head
#     while temp:
#         if zcnt:
#             temp.data = 0
#             zcnt -= 1
#         elif ocnt:
#             temp.data = 1
#             ocnt -= 1
#         else:
#             temp.data = 2
#             tcnt -= 1
#         temp = temp.next
#     return head