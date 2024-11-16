"""
A linked list is a linear data structure where elements, called nodes, are connected by pointers. 
Each Node contains:
    Data : The value of the node 
    pointer or reference : A link to the next node in sequnece 

Types of Linked Lists

    Singly Linked List: Each node points to the next node in the list.
    Doubly Linked List: Each node points to both the previous and the next node.
    Circular Linked List: The last node points back to the first node, forming a circle.

pros ;
    Dynamic Size: Linked lists can grow or shrink in size dynamically.
    Efficient Insertions/Deletions: Adding or removing elements is easier (no shifting required) compared to arrays.
    Flexible Memory Usage: Memory allocation is not contiguous.

"""

# Structur of single link lise 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    

def insert_at_beginning(head, data):
    new_node = Node(data) 
    new_node.next = head  
    return new_node        

def insert_at_end(head , data):
    new_node = Node(data= data)
    if not head:
        return new_node
    temp  = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    return head        

def delete_node(head, value):
    if not head:
        return None 
    if head.data == value:
        return head.next
    temp = head
    while temp.next and temp.next.data != value:
        temp =temp.next

    if temp.next:
        temp.next = temp.next.next

    return head


def traverse(head):
    temp =  head
    while temp:
        print(temp.data , end='->')
        temp =temp.next

    print(None )

head = None
head = insert_at_beginning(head, 10)
head = insert_at_beginning(head, 20)
head = insert_at_beginning(head , 30)
head = delete_node(head, 10)
head = insert_at_end(head, 30)
traverse(head)


