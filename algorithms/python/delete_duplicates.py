# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def delete_duplicates(self, head: ListNode) -> ListNode:
    node = head
    
    while node != None:
        if node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            
            if node.next:
                if node.val == node.next.val:
                    continue

        node = node.next
    
    return head
