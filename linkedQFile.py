class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_elements(self):
        return self.value

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def __str__(self):
        x = ""
        z = ""
        y = self.__first
        count = 1
        while y != None :
            x = str(y.get_elements())
            z = z+ " " + x
            y = y.next
            count+=1
        return z


    def enqueue(self, value):
        new = Node(value)
        if self.__first == None:
            self.__first = new
            self.__last = new

        else:
            self.__last.next = new
            self.__last = new
    
    def isEmpty(self):
        if self.__first == None:
            return True
        else:
            return False
        
    def dequeue(self):
        if not self.isEmpty():
            x = self.__first.get_elements()
            self.__first = self.__first.next

            return x
        else:
            return "Queue is empty"
        
    def size(self):
        y = self.__first
        lenght = 0 
        while y:
            lenght += 1
            y = y.next
        return lenght
    
    def display(self):
        y = self.__first
        count = 1
        while y != None :
            print('Entry # ', count, '=', y.get_elements()) 
            y = y.next
            count+=1

            
