class Node:
    def __init__(self,a,b):
        self.elem=a
        self.next=b
        
def createnode(a):
    head=Node(a[0],None)
    tail=head
    for i in range(1,len(a)):
        n=Node(a[i],None)
        tail.next=n
        tail=tail.next
    return head


def printnode(a):
    head=a
    tail=head
    while tail!=None:
        print(tail.elem)
        tail=tail.next
def changenode(a,idx):
    head=a
    tail=head
    tail1=head
    tail2=head
    c=0
    c1=0
    while tail!=None:
        tail=tail.next
        c+=1
        
    #print(c)
    while tail1!=None:
        
        if c1+1==c:
            temp=tail1
            
            tail1=None
            #print(temp.elem)
            c1+=1
        else:
        
            tail1=tail1.next
            c1+=1 
             
        
    while tail2!=None:
        if idx==0:
            
            temp.next=head
            head=temp
            #print(temp.elem)
            return head 
    

def copynode(a):
    head=a
    tail=head
    copy_head=None
    copy_tail=None
    while tail!=None:
        n=Node(tail.elem,None)
        if copy_head==None:
            copy_head=n
            copy_tail=n
            copy_tail.next=tail.next
            copy_tail=copy_tail.next
            
        else:
            copy_tail.next=tail.next
            copy_tail=copy_tail.next            
            
            
        tail=tail.next 
    return copy_head  



def reverse_out_of_place(a):
    head=a
    tail=head
    new_head=Node(head.elem,None)
    temp=head.next
    while temp!=None:
        n=Node(temp.elem,new_head)
        #print(temp.elem)
        new_head=n
        temp=temp.next  
    return new_head  
    

def reverse_in_place(a):
    head=a
    tail=head
    prev=None
    while tail!=None:
        store_var=tail.next #tail.next store kortesi cz pore use korbo
        tail.next=prev
        prev=tail
        print(prev.elem)
        tail=store_var       #tail.next ar kaj kortesi aita diye
    return prev
    
    
    
        
x=createnode([1,2,3,4,9])
#printnode(x)
#z=changenode(x,0)
#printnode(z)
#q=copynode(x)
#printnode(q)
w=reverse_out_of_place(x)
#printnode(w)
e=reverse_in_place(x)
#printnode(e)
class Node:
    def __init__(self,a,b):
        self.elem=a
        self.next=b
        
def createnode(a):
    head=Node(a[0],None)
    tail=head
    for i in range(1,len(a)):
        n=Node(a[i],None)
        tail.next=n
        tail=n
    return head


def printnode(a):
    head=a
    tail=head
    while tail!=None:
        print(tail.elem)
        tail=tail.next
    

def insertelem(head, ele, idx):
    head=head
    tail=head
    tail1=head
    c=0
    
    while tail!=None:
        if idx == 0:
            new_node = Node(ele, head)
            head = new_node
            return head
            
        if idx>0:
            if c+1==idx:
                new_node = Node(ele, tail.next)
                tail.next=new_node
        tail=tail.next
        c+=1      
    return head

def removelem(a,b):
    
    head=a
    tail=head
    idx=b
    
    c=0
    while tail!=None:
        if idx==0:
            head=head.next
            return head
        if idx>0:
            if c+1==idx:
                tail.next=tail.next.next

        c+=1
        tail=tail.next
    return head

def nodeat(head,idx):
    head=head
    tail=head
    c=0
    while tail!=None:
        if c==idx:
            temp=tail
            return temp
        c+=1
        tail=tail.next

def printelem(head,idx):
    head=head
    tail=head
    c=0
    while tail!=None:
        if c==idx:
            n=nodeat(head,idx)
            #print(n.elem)
        c+=1
        tail=tail.next
    
def removesomething(head,idx):
    head=head
    tail=head
    c=0
    while tail!=None:
        if idx==0:
            head=head.next
        if idx>0:
            if c==idx:
                n1=nodeat(head,idx-1)
                n2=nodeat(head,idx+1)
                n1.next=n2
        c+=1
        tail=tail.next
    return head
                

x = createnode([1, 2,6, 3, 4])
#y = insertelem(x, 10, 1)
#printnode(y)
print('============')
#z=removelem(x,0)
#printnode(z)
printelem(x,2)
m=removesomething(x,3)
printnode(m)





class Solution(object):
    def removeElements(self, head, val):
        head=head
        tail=head
        while tail!=None:
            if head.val==val:
                head=head.next
            elif tail.next.val==val:
                tail.next=tail.next.next
            tai=tail.next
        return head

        











        







    