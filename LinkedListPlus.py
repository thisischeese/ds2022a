from http.client import NETWORK_AUTHENTICATION_REQUIRED
from re import X


class ListNode:
    def __init__(self, newItem, nextNode:'ListNode'):
        self.item = newItem
        self.next = None
class LinkedListPlus:
    def __init__(self):
        self.__head = None
        self.__numItems =0

    def insert(self, i:int, newItem):
        if i>0 and i<=self.__numItems:
            prev = self.__getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        elif(i==0):
            newNode = ListNode(newItem, self.__head)
            #self.__head.next = newNode
            self.__numItems += 1
        else:
            print("index", i, "out of bound in insert()")
            
    def append(self, newItem):
        if(self.__head==None):
            newNode = ListNode(newItem, self.__head)
            #self.__head.next = newNode
            self.__numItems += 1
        else:
            prev=self.__getNode(self.__numItems-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems +=1

    def pop(self, i:int):
        if (i>0 and i<=self.__numItems -1):
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -=1
            return retItem
        elif(i==0):
            curr = self.__head
            self.__head.next = self.__head.next.next
            retItem = curr.item
            self.__numItems -=1
            return retItem
        else:
            return None
        
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr!=None:
            prev.next = curr.next
            self.__numItems -=1
            return x
        else:
            return None
        
    def get(self, i:int):
        if (self.isEmpty() or i==0):
            return None
        if (i>0 and i<=self.__numItems-1):
            return self.__getNode(i).item
        else:
            return None

    def index(self,x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item ==x:
                return index
            else:
                curr = curr.next
        return -2

    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__head = ListNode("dummy",None)
        self.__numItems =0
    
    def count (self, x) -> int:
        cnt=0
        curr = self.__head.next
        while curr !=None:
            if curr.item ==x:
                cnt+=1
            curr = curr.next
        return cnt
    
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))
            
    def copy(self):
        a=LinkedListPlus()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    
    def reverse(self):
        a = LinkedListPlus()
        for index in range(self.__numItems):
            a.insert(0,self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))
            
    def sort(self) -> None:
        a=[]
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])
            
    def __findNode(self,x) -> (ListNode,ListNode):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return (prev,curr)
            else:
                prev = curr; curr = curr.next
        return (None,None)
    
    def __getNode(self, i:int) -> ListNode:
        curr = self.__head.next
        if (i==0):
            return None
        else:
            for index in range(i):
                curr = curr.next
            return curr
    
    def printList(self):
        curr = self.__head.next
        while curr!=None:
            print(curr.item,end=' ')
            curr = curr.next
        print()