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
    
    def get (self, index):
        if index < 0 or index >= self.length:
            return None  
        if index < self.length/2 :
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length, index+1, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        temp.value = value
        return True
    
    def insert (self, index, value):
        if index < 0 or index > self.length:
            return None  
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        new_node = Node(value)
        before = self.get(index-1)
        new_node.next = before.next
        new_node.prev = before
        before.next.prev = new_node
        before.next = new_node
        self.length +=1
        return True
    
    def remove (self, index):
        if index < 0 or index >= self.length:
            return None  
        if index == 0:
            self.pop_first()
            return True
        if index == self.length-1:
            self.pop()
            return True
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -=1
        return temp