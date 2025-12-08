class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        
class Queued_list:
    def __init__ (self, value):
        new_node = Node(value)
        self.last = new_node
        self.first = new_node
        self.queue = 1
        
    def queued (self, value):
        new_node = Node(value)
        if self.queue ==0:
            self.last = new_node
            self.first = new_node
        else:
            new_node.next = self.last
            self.last = new_node
        self.queue += 1
        
    def dequeued (self):
        temp = self.last
        while temp:
            