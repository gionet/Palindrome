import time

# TWO POINTER METHOD: FAST & SLOW
# O(n) time
# O(1) space

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        left, right = head, prev
        while right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next
        return True

def main():  
    # InputString = 'a@b!!b$a'
    # TrashSymbolsString = '!@$'

    InputString = input('InputString: ') 
    TrashSymbolsString = input('TrashSymbolsString: ')
    
    head = None
    tail = None
    
    InputString = InputString.replace(' ', '') # Remove all spaces
    
    for char in InputString.lower().strip():
        if char not in TrashSymbolsString:
            if not head:
                head = ListNode(char)
                tail = head
            else:
                tail.next = ListNode(char)
                tail = tail.next

    solution = Solution()
    result = solution.isPalindrome(head)
    print(result)
    
main()
    
# if __name__ == '__main__':
#     num_iterations = 100000
#     total_execution_time = 0

#     for _ in range(num_iterations):
#         start_time = time.time()
#         main()
#         end_time = time.time()
#         execution_time = end_time - start_time
#         total_execution_time += execution_time

#     average_execution_time = (total_execution_time / num_iterations) * 1000  # in milliseconds
#     print(f"Average execution time over {num_iterations} iterations: {average_execution_time:.10f} ms")