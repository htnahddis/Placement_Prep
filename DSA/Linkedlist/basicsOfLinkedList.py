#coming from c++ i know 
"""
class Node{
    int data;
    Node* next;

    Node ( int val){
    data = val;
    next = Null;}
}



"""

#Similarly for python:

class ListNode:
    def __init__(self, value):
        self.value = value;
        self.next = None


node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3
print(node1.value, node1.next)

#basic operations 
"""Inserting Start"""

node4 = ListNode(40)

node4.next = node1

print(f"Node inserted at the start: ${node4.value} ${node4.next.value}")


"""Inserting at end"""
node5 = ListNode(50)

temp = node1

while temp:  #one mistak i did here, i used temp.next, which immediaelty start from 2nd node. might create some loss 

    temp = temp.next

temp.next = node5
print(f"Node inserted at the end: ${temp.value} ${temp.next.value}")


"""Deleting at end"""
temp = node1

while temp.next:  #one mistak i did here, i used temp.next, which immediaelty start from 2nd node. might create some loss 

    temp = temp.next

temp



