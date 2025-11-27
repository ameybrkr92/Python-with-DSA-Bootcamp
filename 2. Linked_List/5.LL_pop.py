class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__ (self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
        

 #       for _ in range(self.length):
 #               if self.tail is None:
                    
    
    
    
    
    
mylinked_list = Linkedlist(8)
print ("---------") 
mylinked_list.print_list()
print(mylinked_list.print_list())
print ("---------")   
mylinked_list.append(12)
mylinked_list.print_list()
print ("---------")     
mylinked_list.append(10)
mylinked_list.print_list()
print ("---------")   
mylinked_list.pop()
mylinked_list.print_list()
print ("---------") 
print("item removed", mylinked_list.pop().value)
print ("---------") 
mylinked_list.print_list()
print ("---------") 
mylinked_list.pop()
mylinked_list.print_list()
print ("---------") 
mylinked_list.pop()
mylinked_list.print_list()