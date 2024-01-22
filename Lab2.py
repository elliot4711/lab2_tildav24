from array import array 

class ArrayQ:
    # Klass för array 

    def __init__(self):
    #     Är konstruktiorn som anropas när en ny array skapas 
    #     Parametrar : array
            self.top = None 
            self._array= array('i') 

    def enqueue(self, value):  
        # Metod som lägger till värde längst bak
        self._array.append(value)
        print(self._array)

    def dequeue(self):
        # Metod som plockar ut det som står först i kön
        return self._array.pop(0)
    
    def isEmpty(self):
        if len(self._array) == 0:
            return True
        else:
            return False

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

if __name__ == '__main__':
    order = input("Vilken ordning är korten? : ")
    order = order.split(",")
    for i in range(len(order)):
        order[i] = int(order[i])   
    #print(order)
    q = ArrayQ()
    a = ArrayQ()
    for i in range(len(order)):
       q.enqueue(order[i])
    print(q.isEmpty() )
    while q.isEmpty() == True: 
        x = q.dequeue()
        q.enqueue(x)
        y = q.dequeue()
        a.enqueue(y)
    


    print(q)


    