class Node :
    def __init__ (self, d):
        self.val=d
        self.next=None

    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while temp!=None :
            print(temp.data)
            temp=temp.next

    def insert_beg(self, d):
        nnode=Node(d)
        if head==None :
            head=nnode
        else :
            nnode.next=self.head
            head=nnode

    def insert_end(self, d):
        nnode=Node(d)
        if head==None :
            head=nnode
        else:
            temp=self.head
            while temp.next!=None :
                temp=temp.next
            temp.next=nnode

    def insert_at(self, d, p):
        
        if p==1 :
            insert_beg(d)
        else:
            nnode=Node(d)
            temp=self.head
            pos=1
            while pos!=p :
                temp=temp.next
                pos+=1
            nnode.next=temp.next
            temp.next=nnode

    def delete_beg(self):
        head=head.next

    def delete_end(self):
        temp=self.head
        while temp.next!=None :
            temp=temp.next
        temp.next=None

    def delete_at(self, p):
        pos=1
        temp=self.head
        if temp.next==None:
            delete_end()
        else :
            while pos!=p :
                temp=temp.next
                pos+=1
            temp.next=temp.next.next

insert_beg(23)
insert_beg(44)
insert_end(88)
insert_end(54)
insert_at(32,3)
printlist()
delete_beg()
delete_end()
insert_end(52)
delete_at(2)
printlist()