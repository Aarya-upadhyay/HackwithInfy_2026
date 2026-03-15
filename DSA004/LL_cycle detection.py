# slow and fast pointer approach
def has_cycle(head):
    
    sp=head
    fp=head
    while fp and fp.next:
        sp=sp.next
        fp=fp.next.next
        if sp==fp:
            return 1
    return 0
        
