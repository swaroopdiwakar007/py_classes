class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def printEnd(self):
        str1 = ""
        while self:
            str1 += str(self.val) + "->"
            self = self.next

        print(str1)

class LinkedList:
    def __init__(self, arr = []):
        self.arr = arr
        self.node = ListNode()
        self.cur = self.node
        for i in arr:
            self.cur.next = ListNode(i)
            self.cur = self.cur.next
        self.node = self.node.next

    def add(self, val):
        self.cur.next = ListNode(val)
        self.cur = self.cur.next
        
    def printList(self):
        dummy = self.node
        str1 = ""
        while dummy:
            str1 += str(dummy.val) + "->"
            dummy = dummy.next
        
        print(str1)
         
    def pop(self):
        self.cur = self.node
        while self.cur.next.next:
            self.cur = self.cur.next
        self.cur.next = None

    def popq(self):
        self.node = self.node.next
