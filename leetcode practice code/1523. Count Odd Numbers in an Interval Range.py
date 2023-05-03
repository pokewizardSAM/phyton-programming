class solution(object):
    def countodds(self,low,high):
        count = (high -low)//2
        if high%2==0 and low%2==0:
            return count
        elif high%2!=0 and low%2!=0:
            return count+1
        else:
            return count+1
        
print(solution().countodds(1,8))