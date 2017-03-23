# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        l3=[0]
        digit=l1.val+l2.val
        l3[0]=(digit)%10
        while l1.next is not None or l2.next is not None:
            try:
                if digit>=10:
                    digit=l1.next.val+l2.next.val+1
                else:
                    digit=l1.next.val+l2.next.val
                l1=l1.next
                l2=l2.next
            except:  #If l1.next or l2.next is NoneType
                try:
                    if digit>=10:
                        digit=l1.next.val+1
                    else:
                        digit=l1.next.val
                    l1=l1.next
                except:
                    if digit>=10:
                        digit=l2.next.val+1
                    else:
                        digit=l2.next.val
                    l2=l2.next
            l3.append(digit%10)
        if digit>=10:
            l3.append(1)
        return l3
#####Below is other's code https://discuss.leetcode.com/topic/8909/clear-python-code-straight-forward
class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next


def divmod(a, b):
    return(a // b, a % b)
