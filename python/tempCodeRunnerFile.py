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
            
            tail1.next=None
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
    
        
x=createnode([1,2,3,4,9])
#printnode(x)
z=changenode(x,0)
printnode(z)
