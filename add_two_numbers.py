class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next        

# Create the linked lists
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

# Link the nodes together
node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6

# Create the solution object
solution = Solution()

# Get the first node of l1
second_node = solution.addTwoNumbers(node1, node4)