import time

# LINKED LIST METHOD
# O(n) time
# O(1) space

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        
        while head:
            nums.append(head.value)
            head = head.next
            
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True
            
def main():  
    InputString = 'sator arepo tenet opera rotas.'
    TrashSymbolsString = ' .,!@$'
    
    head = None
    tail = None
    
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

# if __name__ == '__main__':
#     num_iterations = 100000
#     total_execution_time = 0

#     # for _ in range(num_iterations):
#     #     start_time = time.time()
#     #     main()
#     #     end_time = time.time()
#     #     execution_time = end_time - start_time
#     #     total_execution_time += execution_time

#     # average_execution_time = (total_execution_time / num_iterations) * 1000  # in milliseconds
#     # print(f"Average execution time over {num_iterations} iterations: {average_execution_time:.10f} ms")