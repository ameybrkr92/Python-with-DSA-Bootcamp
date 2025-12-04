class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class Double_linkedlist:
    def __init__ (self, value):
        new_node = Node (value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list (self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
    def append (self, value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend (self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop (self):
        if self.length ==0:
            return None
        if self.length ==1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        temp = self.tail
        temp.prev.next = None
        self.tail = temp.prev
        temp.prev = None
        self.length -= 1
        return temp
    
    def pop_first(self):
        if self.length ==0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        temp = self.head
        temp.next.prev = None
        self.head = temp.next
        temp.next = None
        self.length -=1
        return temp