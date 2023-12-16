class Solution(object):
    def average(self, salary):
        salary.remove(min(salary))
        salary.remove(max(salary))
        output = sum(salary)/len(salary)
        return output
    
salary = [4000,3000,1000,2000]

print(Solution().average(salary))




