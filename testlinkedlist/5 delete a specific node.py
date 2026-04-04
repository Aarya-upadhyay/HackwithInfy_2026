def deleteNode(llist, position):
    # Case 1: delete head
    if position == 0:
        return llist.next
    
    current = llist
    count = 0
    
    # Move to (position - 1)
    while count < position - 1:
        current = current.next
        count += 1
    
    # Delete node
    current.next = current.next.next
    
    return llist
  
