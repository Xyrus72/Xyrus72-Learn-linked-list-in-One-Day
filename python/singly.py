
class Node:
  def __init__(self,elem,next = None):
    self.elem, self.next = elem,next

class Node:
  def __init__(self,elem,next = None):
    self.elem, self.next = elem,next
class LinkedList:
  def __init__(self,arr):
    self.head = Node(arr[0])
    tail = self.head
    for i in range(1,len(arr)):
      newNode = Node(arr[i])
      tail.next = newNode
      tail = newNode

  def printLinkedList(self):
    temp = self.head
    while temp != None:
      if temp.next != None:
        print(temp.elem, end = '-->')
      else:
        print(temp.elem)
      temp = temp.next

  def countNodes(self):
    head=self.head
    tail=head
    c=0
    while tail!=None:
        c+=1
        tail=tail.next
    return c

  def nodeAt(self, idx):
    head=self.head
    tail=head
    c=0
    while tail!=None:
        if c==idx:
            temp=tail
            return temp
        c+=1
        tail=tail.next

  def elemAt(self,idx):
    head=self.head
    tail=head
    c=0
    while tail!=None:
        if c==idx:
            return tail.elem
        c+=1
        tail=tail.next

  def indexOf(self,value):
    head=self.head
    tail=head
    c=0
    key=0
    while tail!=None:
        if tail.elem==value:
            key+=1
            return c
        c+=1
        tail=tail.next
    if key==0:
        return -1

  def contains(self,value):
    head=self.head
    tail=head
    while tail!=None:
        if tail.elem==value:
            return True
        tail=tail.next
    return False

  def insert(self, value, idx): #Done for students
    head=self.head
    tail=head
    c=0
    n=Node(value,None)
    while tail!=None:
        if idx == 0:
            if c == idx:
                n.next =self. head
                self.head = n
                return self.head  # Add this line

                
                
        elif idx>0:
            if c+1==idx:
                temp1=self.nodeAt(c)
                temp2=self.nodeAt(c+1)
                temp1.next=n
                n.next=temp2
        c+=1
        tail=tail.next
    return self.head







  def remove(self,idx):
    tail=self.head
    c=0
    while tail!=None:
        if idx==0:
            if c==idx:
                self.head=self.head.next
        elif idx>0 :
            if c+1==idx:
                tail.next=tail.next.next
        c+=1
        tail=tail.next
    return self.head

  def rotateRight(self):
    head=self.head
    tail=head
    tail1=head
    c=0
    while tail.next!=None:
        c+=1
        tail=tail.next
      
    xy=self.nodeAt(c)
    y=self.nodeAt(c-1)
    d=0
    while tail1!=None:
        if d==0:
            
            xy.next=self.head   
            self.head=xy
            
            
        if tail1==y:
            tail1.next=None
        d+=1 
        tail1=tail1.next
    return self.head



  def rotateLeft(self):
    pass



print('Create Linked List')
l1 = LinkedList(([10,34,21,6,-2]))
l1.printLinkedList()
print()

print('Count Nodes of Linked List')
print(l1.countNodes())
print()

print('Find out the node at a certain index')
n = l1.nodeAt(3)
print('Node at index 3:', end = ' ')
print(n.elem if n!=None else 'Invalid Index')
print('Corner Cases:')
print('Node at index -1:', end = ' ')
n = l1.nodeAt(-1)
print(n.elem if n!=None else 'Invalid Index')
print('Node at index 5:', end = ' ')
n = l1.nodeAt(5)
print(n.elem if n!=None else 'Invalid Index')
print()

print('Find out the element at a certain index')
print('Element at index 1:', end = ' ')
print(l1.elemAt(1))
print('Corner Cases:')
print('Element at index -2:', end = ' ')
print(l1.elemAt(-2))
print('Element at index 6:', end = ' ')
print(l1.elemAt(6))
print()

print('Find out the index of an element')
print('Index of element -2', end = ' ')
print(l1.indexOf(-2))
print('Corner Cases:')
print('Index of element 23', end = ' ')
print(l1.indexOf(23))
print()

print('Find out the if linked list contains an element')
print('Linked List contains -2:', end = ' ')
print(l1.contains(-2))
print('Corner Cases:')
print('Linked List contains 3:', end = ' ')
print(l1.contains(3))
print()

print('Insert element in certain index')
print('Insert 41 at index 2:', end = ' ')
l1.insert(41,2)
l1.printLinkedList()
print('Corner Cases:')
print('Insert 25 at index 0:', end = ' ')
l1.insert(25,0)
l1.printLinkedList()
print('Insert 15 at index 7:', end = ' ')
l1.insert(15,7)
l1.printLinkedList()
print('Insert 27 at index -1:', end = ' ')
l1.insert(27,-1)
l1.printLinkedList()
print()

print('Delete node from a certain index')
print('Delete from index 5:', end = ' ')
l1.remove(5)
l1.printLinkedList()
print('Corner Cases:')
print('Delete from index 0:', end = ' ')
l1.remove(0)
l1.printLinkedList()
print('Delete from index 5:', end = ' ')
l1.remove(5)
l1.printLinkedList()
print('Delete from index -1:', end = ' ')
l1.remove(-1)
l1.printLinkedList()
print()

print('Right Rotate')
l1.rotateRight()
l1.printLinkedList()
print()

print('Left Rotate')
l1.rotateLeft()
l1.printLinkedList()
print()











