def insertNodeAtPosition(llist, data, position):
    # Write your code here
    n=SinglyLinkedListNode(data)
    if position==0:
        n.next=llist
        return llist
    curr=llist
    c=0
    while curr is not None and c<position-1:
        curr=curr.next
        c+=1
    n.next=curr.next
    curr.next=n
    return llist
