class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        oddNode=head
        evenNode,t=head.next,head.next
        while evenNode.next!=None and evenNode.next.next!=None:
            oddNode.next=evenNode.next
            evenNode.next=oddNode.next.next
            oddNode=oddNode.next
            evenNode=evenNode.next
        if evenNode.next!=None:
            oddNode.next=evenNode.next
            oddNode=oddNode.next
        oddNode.next=t
        evenNode.next=None
        return head
        