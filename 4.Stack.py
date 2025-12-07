class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        
class stacked_list:
    def __init__ (self, value):
        new_node = Node (value)
        self.bottom = new_node
        self.top = new_node
        self.height = 1
        
    def push (self, value):
        new_node = Node(value)
        if self.height == 0:
            self.bottom = new_node
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1
        return True
    
    def pop (self):
        if self.height == 0:
            return None
        if self.height == 1:
            temp = self.top
            self.top = None
            self.bottom = None
            self.height = None
            return temp
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp