class solution:
         def Rev_Linkedlist(head): # function defined to reverse a linked list 
                # three pointers to manage position 
                curr=head
                next=None
                prev=None
                while curr:
                        next=curr.next
                        curr.next=prev
                        prev=curr
                        curr=next 
                return curr
""" passed 85%"""
