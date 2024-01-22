from array import array 
#from arrayQFile import ArrayQ
from linkedQFile import LinkedQ

if __name__ == '__main__':
    order = input("Vilken ordning är korten? : ")
    order = order.split(",")
    for i in range(len(order)):
        order[i] = int(order[i])   
    #q = ArrayQ()
    #a = ArrayQ()
    q = LinkedQ()
    a = LinkedQ()
    for i in range(len(order)):
       q.enqueue(order[i])
    while q.isEmpty() == False: 
        x = q.dequeue()
        q.enqueue(x)
        y = q.dequeue()
        a.enqueue(y)

print(a)


# Kort ska vara i ordning 7,1,12,2,8,3,11,4,9,5,13,6,10

