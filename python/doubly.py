import numpy as np
class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p
class DoublyList:

  # Creates a Dummy Head for Dummy Headed Circular Doubly Circular Linked List.
  def __init__(self):
    self.dummy_head=Node(None,None,None)


  #create a DHDCL from an array
  def create_list(self, l):
    head=Node(l[0],None,None)
    tail=head
    for i in range (1,len(l)):
        n=Node(l[i],None,None)
        tail.next=n
        tail.next.prev=tail
        tail=tail.next
    tail.next=head
    head.prev=tail
    self.dummy_head=head
    #return head




  # Counts the number of Nodes in the list and return the number
  def countNode(self):
    head=self.dummy_head
    tail=head
    c=0
    while tail!=None:
      c+=1
      tail=tail.next
      if tail==head:
        return c
        break
      


  # prints the elements in the list forward
  def forwardprint(self):
    head=self.dummy_head
    tail=head
    #print(head)
    #print('ssssssssssssssssssssssssss')
    while tail!=None:
        #print(tail)
        print(tail.element)
        tail=tail.next
        if tail==head:
            break


  # prints the elements in the list backward
  def backwardprint(self):
    head=self.dummy_head
    tail=head
    while tail!=None:
      tail=tail.prev
      print(tail.element)
      if tail==head:
        break
      


  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    head=self.dummy_head
    tail=head
    
    c=0
    while tail!=None:
      if c==idx:
        temp=tail
        return temp
      c+=1
      tail=tail.next
      if tail==head:
        break
    


  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    head=self.dummy_head
    tail=head
    count=0
    
    while tail!=None:
      if tail.element==elem:
        return count
      tail=tail.next
      count+=1
      if tail==head:
        break
   
    if elem>count:
      return -1 


  # insert at specific index of the DHDCL
  def insert(self, elem, idx):
    head=self.dummy_head
    tail=head
    n=Node(elem,None,None)
    c=0
    while tail!=None:
      if idx==0:
        if c==idx:
          n.next=head
          n.prev=head.prev
          head.prev.next=n
          head.prev=n
          head=n
          tail=head
          self.dummy_head=head
      elif idx>0:
        if c+1==idx:
          n.next=tail.next
          n.prev=tail
          tail.next.prev=n
          tail.next=n
          
          
      c+=1
      tail=tail.next
      if tail==head:
        break
      
      


  #removes the node of the specific index and returns the element of the node
  def remove(self, idx):
    head=self.dummy_head
    tail=head
    c=0
    while tail!=None:
      if idx==0:
        if c==idx:
          remove=head.element
          head.prev.next=head.next
          head.next.prev=head.prev
          head=head.next
          self.dummy_head=head
          tail=head
          
      elif idx>0:
        if c+1==idx:
          remove=tail.next.element
          tail.next=tail.next.next
          tail.next.prev=tail
      c+=1
      tail=tail.next
      if tail==head:
        return remove
        

  
  
  
  
print("///  Test 01  ///")
h1 = DoublyList() # Creates a dummy headed doubly circular linked list
h1.create_list(np.array([10,20,30,40]))
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 10,20,30,40.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 40,30,20,10.
print('Total Nodes: ', end = ' ')
print(h1.countNode()) # This should print: 4
print()

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
print('Node at 2nd index: ', end = ' ')
n = h1.nodeAt(2)
print(n.element if n!=None else 'Index Error')# This should print: 30.
print('Node at 0th index: ', end = ' ')
n = h1.nodeAt(0)
print(n.element if n!=None else 'Index Error')# This should print: 10. IGNORE DUMMY HEAD
print('Node at -1th index: ', end = ' ')
n = h1.nodeAt(-1)
print(n.element if n!=None else 'Index Error')# This should print "index error"
print()

print("///  Test 03  ///")
print('Index of element 40:', end = ' ')
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that
print('Index of element 6:', end = ' ')
index = h1.indexOf(6)
print(index) # doesn't exists in the list this will print -1.
print()

print("///  Test 04  ///")
print('Inserting 85 in 0th index')
h1.insert(85,0)
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 85,10,20,30,40.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 40,30,20,10,85.

print()
print('Inserting 95 in 3rd index')
h1.insert(95,3)
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 85,10,20,95,30,40.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 40,30,95,20,10,85.

print()
print('Inserting 75 in 6th index')
h1.insert(75,6)
print('Forward Print: ', end = ' ')
h1.forwardprint() # This should print: 85,10,20,95,30,40,75.
print('Backward Print: ', end = ' ')
h1.backwardprint() # This should print: 75,40,30,95,20,10,85.
print()


print("///  Test 05  ///")
h2 = DoublyList() # uses the constructor
h2.create_list(np.array([10, 20, 30, 40, 50, 60, 70]))
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 10,20,30,40,50,60,70.
print()

print('Removing node from 0th index')
print("Removed element: "+ str(h2.remove(0))) # This should print: Removed element: 10
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 20,30,40,50,60,70.
print('Backward Print: ', end = ' ')
h2.backwardprint() # This should print: 70,60,50,40,30,20.
print()

print('Removing node from 3rd index')
print("Removed element: "+ str(h2.remove(3))) # This should print: Removed element: 50
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 20,30,40,60,70.
print('Backward Print: ', end = ' ')
h2.backwardprint() # This should print: 70,60,40,30,20.
print()

print('Removing node from 4th index')
print("Removed element: "+ str(h2.remove(4))) # This should print: Removed element: 70
print('Forward Print: ', end = ' ')
h2.forwardprint() # This should print: 20,30,40,60.
print('Backward Print: ', end = ' ')
h2.backwardprint() # This should print: 60,40,30,20.
print()