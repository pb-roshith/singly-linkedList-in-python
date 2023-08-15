class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Link:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end=" ")
                temp=temp.next
    
    def addFirst(self, val):
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
        
    def addLast(self, val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newNode
    
    def insertPos(self, pos, val):
        if(pos==0):
            self.addFirst(val)
        else:
            newNode=Node(val)
            temp=self.head
            for i in range(0,pos-1):
                temp=temp.next
            newNode.next=temp.next
            temp.next=newNode
    
    def delete(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
        
    def search(self, val):
        temp=self.head
        i=0
        while temp is not None:
            if(temp.data==val):
                print("the element is at position ", i)
                return
            i+=1
            temp=temp.next
            
    def contains(self, val):
        temp=self.head
        i=0
        while temp is not None:
            if(temp.data==val):
                print(True)
                return
            i+=1
            temp=temp.next
        else:
            print(False)
            
    def get(self, pos):
        temp=self.head
        for i in range(pos):
            temp=temp.next
        print(temp.data)
        
    def update(self, pos, val):
        temp=self.head
        for i in range(pos):
            temp=temp.next
        temp.data=val
        
    def deletePos(self, pos):
        if self.head==None:
            print("list is empty")
            return
        if pos==0:
            self.head=self.head.next
            return
        temp=self.head
        pre=None
        for i in range(pos):
            pre=temp
            temp=temp.next
        pre.next=temp.next
        
l=Link()
l.addFirst(100)
l.addLast(200)
l.addLast(300)
l.addFirst(10)
l.insertPos(0,500)
l.delete()
l.display()
l.search(10)
l.contains(90)
l.contains(10)
l.get(1)
l.update(3,800)
l.display()
print()
l.deletePos(2)
l.display()