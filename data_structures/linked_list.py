class LinkedList:

    def __init__(self, head):
        self.head = head
        self.current_element = self.head

    # Node navigation
    def next(self):
        if self.current_element.next is None:
            return
        self.current_element = self.current_element.next
    
    def go_back_to_head(self):
        self.current_element = self.head

    # Node queries
    def get_current_element(self):
        return self.current_element.data

    # Subordinate classes
    class Node:
        """A Node has two properties:
        `data` which represents the instance of data stored in the node
        `next` which is a pointer to the next node
        """
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next




if __name__ == '__main__':

    data_set = ['alex', 'siobhan', 'lucy', 'rosie']

    linked_list = LinkedList(head=LinkedList.Node(data='alex', next=None))
    linked_list.head.next = LinkedList.Node(data='siobhan')
    
    print(linked_list.get_current_element())
    linked_list.next()
    print(linked_list.get_current_element())
    linked_list.go_back_to_head()
    print(linked_list.get_current_element())
    
