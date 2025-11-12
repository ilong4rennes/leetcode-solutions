# Last updated: 11/12/2025, 3:53:13 AM
class MyLinkedList:
    
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        dummy = self.head.next
        for _ in range(index):
            dummy = dummy.next
        return dummy.val

    def addAtHead(self, val: int) -> None:
        newHead = self.Node(val)
        newHead.next = self.head.next
        self.head.next = newHead
        if self.size == 0: self.tail = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newTail = self.Node(val)
        if self.size == 0:
            self.head.next = newTail
            self.tail = newTail
        else:
            dummy = self.head.next
            for _ in range(self.size - 1):
                dummy = dummy.next
            dummy.next = newTail
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: return
        newNode = self.Node(val)
        dummy = self.head
        for _ in range(index):
            dummy = dummy.next
        newNode.next = dummy.next
        dummy.next = newNode
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        dummy = self.head
        for _ in range(index):
            dummy = dummy.next
        dummy.next = dummy.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)