# --------------------------------------------
# problem-1


# def isPalindrome(head):------------------------using extra data structure
#     # write your code here
#     j = []
#     temp = head
#     while temp != None:
#         j.append(temp.data)
#         temp=temp.next
#     k = j.copy()
#     k.reverse()
#     # print(j)
#     # print(k)
#     return j == k

# def isPalindrome(head):------------------optimal solution
    # def reverse(ptr):
    #     pre = None
    #     nex = None
    #     while ptr != None:
    #         nex = ptr.next
    #         ptr.next = pre
    #         pre = ptr
    #         ptr = nex
    #     return pre
    # if head == None or head.next == None:
    #     return True
    # slow = head
    # fast = head
    # while fast.next != None and fast.next.next != None:
    #     slow = slow.next
    #     fast = fast.next.next
    # slow.next = reverse(slow.next)
    # slow = slow.next
    # dummy = head
    # while slow != None:
    #     if dummy.val != slow.val:
    #         return False
    #     dummy = dummy.next
    #     slow = slow.next
    # return True

# --------------------------------------------
# problem-2


# def removeKthNode(head, n):
#     # Write your code here.
#     start = Node()
#     start.next = head
#     fast = start
#     slow = start
#     for i in range(1, n+1):
#         fast = fast.next
#     while fast.next != None:
#         fast = fast.next
#         slow = slow.next
#     slow.next = slow.next.next
#     return start.next