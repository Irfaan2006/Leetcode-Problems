# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        result = []

        # Take all values from all linked lists
        for head in lists:
            current = head

            while current:
                result.append(current.val)
                current = current.next

        # Sort all values
        result.sort()

        # Create the final linked list
        dummy = ListNode(0)
        current = dummy

        for value in result:
            current.next = ListNode(value)
            current = current.next

        return dummy.next
        