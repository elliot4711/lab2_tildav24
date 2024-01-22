from array import array 
class ArrayQ:
    """
    Class for array
    """

    def __init__(self):
        """
        Constructor for ArrayQ class
        Parameters: self
        Returns: nothing
        """
        
        self.top = None 
        self.Queue()
    
    def Queue(self):
        """
        Creates empty queue instance
        Parameters: self
        Returns: nothing 
        """
        
        self.__array= array('i') 
    
    def __str__(self):
        """
        Returns a string when printing class instance
        Parameters: self
        Returns: List of all array objects
        """

        return str(self.__array.tolist())

    def enqueue(self, value):  
        """
        Function that adds value to the end of array
        Parameters: self, value(to be added)
        Returns: nothing
        """

        self.__array.append(value)
        #print(self.__array)

    def dequeue(self):
        """
        Function that removes the first value in the array and returns its value
        Parameters: self
        Returns: Removed object
        """

        if not self.isEmpty():
            return self.__array.pop(0)
        else:
            print("Queue is empty")
    
    def isEmpty(self):
        """
        Function that checks if array is empty
        Parameters: self
        Returns: True if list is empty, False if not
        """
        
        if len(self.__array) == 0:
            return True
        else:
            return False
    
    def size(self):
        """
        Function that checks the lenght of the array
        Parameters: self
        Returns: Lenght of array
        """

        return len(self.__array)
        
if __name__ == "__main__":
    def test_():
        """
        Test code for arrayQ class
        Parameters: None
        Returns:  nothing
        """

        q = ArrayQ()
        q.enqueue(1)
        q.enqueue(2)
        x = q.dequeue()
        y = q.dequeue()
        if (x == 1 and y == 2):
            print("OK")
        else:
            print("FAILED")