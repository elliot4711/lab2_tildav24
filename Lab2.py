from array import array 
#from arrayQFile import ArrayQ
from linkedQFile import LinkedQ
#import sys

if __name__ == '__main__':
    #order = sys.stdin.readline()
    order = input("Ange ordning på korten: ")
    order = order.split(" ")
    #for i in range(len(order)):
        #order[i] = int(order[i])   
    #q = ArrayQ()
    #a = ArrayQ()
    q = LinkedQ() #Creates linked queue object
    a = LinkedQ() #Creates linked queue object
    for i in range(len(order)): #Adds all values from user input to a queue
       q.enqueue(order[i]) 
    while q.isEmpty() == False: #Performs magic trick
        x = q.dequeue()
        q.enqueue(x)
        y = q.dequeue()
        a.enqueue(y)

print(a) #Prints card order after trick


#Cards should be in order 7 1 12 2 8 3 11 4 9 5 13 6 10

