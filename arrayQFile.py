from array import array 
class ArrayQ:
    # Klass för array 

    def __init__(self):
    #     Är konstruktiorn som anropas när en ny array skapas 
    #     Parametrar : array
            self.top = None 
            self.Queue()
    
    def Queue(self):
        self._array= array('i') 
    
    def __str__(self):
        return str(self._array.tolist())

    def enqueue(self, value):  
        # Metod som lägger till värde längst bak
        self._array.append(value)
        #print(self._array)

    def dequeue(self):
        # Metod som plockar ut det som står först i kön
        if not self.isEmpty():
            return self._array.pop(0)
        else:
            print("Queue is empty")
    
    def isEmpty(self):
        if len(self._array) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self._array)
        
if __name__ == "__main__":
    def test_():
        q = ArrayQ()
        q.enqueue(1)
        q.enqueue(2)
        x = q.dequeue()
        y = q.dequeue()
        if (x == 1 and y == 2):
            print("OK")
        else:
            print("FAILED")