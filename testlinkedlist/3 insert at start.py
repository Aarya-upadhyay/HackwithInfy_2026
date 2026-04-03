def insertNodeAtHead(llist, data):
    # Write your code here
    new_node=SinglyLinkedList(data)
    
    new_node.next=llist
    llist=new_node
    
    return new_node
