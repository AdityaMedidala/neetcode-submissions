class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        head1=list1
        current1=head1
        head2=list2
        current2=head2
        while current1 and current2:
            x=current1.val
            y=current2.val
            if x>y:
                arr.append(y)
                current2=current2.next
            if x<y:
                arr.append(x)
                current1=current1.next
            if x==y:
                arr.append(x)
                arr.append(y)
                current1=current1.next
                current2=current2.next
        while current1:
            x=current1.val
            arr.append(x)
            current1=current1.next
        while current2:
            y=current2.val
            arr.append(y)
            current2=current2.next
        if arr:
            head=ListNode(arr[0])
            current=head
            for value in arr[1:]:
                current.next=ListNode(value)
                current=current.next
            return head


                

            
