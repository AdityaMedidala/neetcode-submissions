# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        arr.reverse()
        if arr:
            head=ListNode(arr[0])
            current=head
            for value in arr[1:]:
                current.next=ListNode(value)
                current=current.next
            return head
        


