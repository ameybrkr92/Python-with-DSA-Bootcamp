class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        
class Linked_list:
    def __init__ (self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp=self.head
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
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend (self, value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop (self):
        if self.length == 0 :
            return None
        temp = self.head
        if self.length ==1 :
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -=1
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        temp =self.head
        self.head = self.head.next
        temp.next = None
        return temp
    
    def get (self, index):
        if index < 0 or index >=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value (self, index, value):
        if index < 0 or index >=self.length:
            return None
        temp = self.get(index)
        temp.value = value
        return None    
            
                 
    def insert (self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        before = self.get(index-1)
        new_node.next = before.next
        before.next = new_node
        self.length +=1
        return True