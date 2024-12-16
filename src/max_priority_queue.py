class MaxHeapq: 
    """
    A class that implements properties and methods 
    that support a max priority queue data structure

    Attributes:
    
    None
    """

    def left(self, i):
        """
        Returns the index of the left child of the element at index i.

        Parameters:
        i (int): Index of the element.

        Returns:
        int: Index of the left child.
        """
        return 2 * i + 1
    
    def right(self, i):
        """
        Returns the index of the right child of the element at index i.

        Parameters:
        i (int): Index of the element.

        Returns:
        int: Index of the right child.
        """
        return 2 * i + 2
    
    def parent(self, i):
        """
        Returns the index of the parent of the element at index i.

        Parameters:
        i (int): Index of the element.

        Returns:
        int: Index of the parent.
        """
        return (i - 1) // 2
    
    def build_max_heap(self, A):
        """
        Builds the maximum heap from the given list.

        Parameters:
        A (list): The list to build the maximum heap from.
        """
        heap_size = len(A)
        for i in range(heap_size // 2 - 1, -1, -1):
            self.heapify(A, i, heap_size)


    def heapify(self, A, i, heap_size):
        """
        Creates a max heap of the list given from the given index. 

        Parameters:
            A (list): The list to be heapified.
            i (int): Index to start heapifying from.
            heap_size (int): Size of the heap.
        """
        left = self.left(i)
        right = self.right(i)

        if left <= (heap_size - 1) and A[left][1] > A[i][1]:
            largest = left
        else:
            largest = i
        if right <= (heap_size - 1) and A[right][1] > A[largest][1]:
            largest = right
        if largest != i:
            A[largest], A[i] = A[i], A[largest] 
            self.heapify(A, largest, heap_size)


    def heappop(self, A):
        """
        Removes and returns the element with the highest priority from the heap
        while maintaining a max-heap.

        Parameters:
        A (list): The heap from which to remove the element.

        Returns:
        tuple: The element with the highest priority.
        """
        if len(A) < 1:
            raise ValueError('Heap underflow: There are no keys in the priority queue ')
        maxk = A[0]
        A[0] = A[-1]
        A.pop()
        self.heapify(A, 0, len(A))
        return maxk


    def heappush(self, A, task):
        """
        Insert a task into the priority queue.

        Parameters:
        A (list): The heap onto which to push the element.
        task (tuple): The element to be pushed onto the heap.
        """
        A.append(task)
        self.change_key(A, len(A) - 1, task[1])
        

    def change_key(self, A, i, key):
        """
        Modifies the priority of the element at index i while maintaining a max-heap.

        Parameters:
        A (list): The heap in which the element exists.
        i (int): Index of the element to be modified.
        key: The new priority of the element.
        """
        A[i] = (A[i][0], key)
        while i > 0 and A[self.parent(i)][1] < A[i][1]:
            j = self.parent(i)
            holder = A[j]
            A[j] = A[i]
            A[i] = holder
            i = j