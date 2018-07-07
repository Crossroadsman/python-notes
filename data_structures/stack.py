class Stack:

    def __init__(self):
        self._data = []

    # User operations
    # ---------------
    def push(self, data):
        """Add a new item to the top of the stack"""
        self._data.insert(0, data)

    def pop(self):
        """Remove and return the top item from the stack"""
        return self._data.pop(0)

    def is_empty(self):
        return len(self._data) == 0

    '''
    def isFull(self):
        """We would implement this if we wanted a maximum size for the
        stack"""
    '''

    def top(self):
        """look at and return the top value of the stack but do not remove
        it"""
        return self._data[0]
