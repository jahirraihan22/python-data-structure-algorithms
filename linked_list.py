class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end (self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    
    def insert_values (self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data) 

    def get_length(self):
        count = 0
        itr = self.head
        while itr: 
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head

        while itr: 
            if count == index - 1:
                itr.next = itr.next.next
                break 

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begin(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def update_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begin(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                self.insert_at(count,data)
                break

            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("List is empty")
            return
            
        itr = self.head
        link_list = ''
        
        while itr:
            link_list += str(itr.data) + '--->'
            itr = itr.next

        print(link_list)

if __name__ == '__main__':
    link_list = LinkedList()
    link_list.insert_values([2,54,23,43,45,32])
    # print("Length: ",link_list.get_length())
    # link_list.remove_at(1)
    link_list.print()
    # link_list.insert_at(5,"BD08")
    link_list.update_at(3,"BD08")
    link_list.print()