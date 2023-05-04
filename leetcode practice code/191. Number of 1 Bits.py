class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return n.bit_count()
    
print(Solution().hammingWeight(0b11111111111111111111111111111101))