def trueorfalse(num):
    length = len(num)

    if length <= 1:
        return True

    increasing = decreasing = True

    for i in range(length):
        for j in range(i+1,length):
            if num[i]>num[j]:
                increasing = False
            if num[i]<num[j]:
                decreasing = False 
            return increasing or decreasing 