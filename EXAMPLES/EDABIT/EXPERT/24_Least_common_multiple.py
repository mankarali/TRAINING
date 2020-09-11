"""
Least Common Multiple
Given a list of integers, create a function that will find the smallest positive integer that is evenly divisible by all the members of the list. In other words, find the least common multiple (LCM).

Examples
lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520

lcm([5]) ➞ 5

lcm([5, 7, 11]) ➞ 385

lcm([5, 7, 11, 35, 55, 77]) ➞ 385
Notes
N/A
"""

def lcm(nums):
    
    a=sorted(list(set(nums)))    
    if len(a)==1: return a[0]
    
    a1=a
    for i in range(len(a)):
        for j in range(1,len(a)):    
            if a[i]!=a[j]:
                if a[j]%a[i]==0:
                    a1[j] = int(a[j]/a[i])
                a1[j]=a[j]

    pf=[]  #Prime Factorization of an Integer    
    for i in a1:
        if i>1:
            num = i
            k=[]
            for i in range(2,num+1):
                while num>1:
                    if num%i == 0:
                        num = num /i
                        k.append(i)
                    else:
                        break 
            pf.append(k)
    
    pf2= sorted(pf,key=len,reverse=True)    
    pf3=pf2[0]
    for i in pf2:
        for j in i:
            if not j in pf3:
                pf3.append(j)

    if a1==sorted(list(set(nums))):
        result=1
        for i in pf3:
            result = result*i
        return (result)
    result=1
    for i in a1:
        result = result*i
    return (result)
#lcm([1]) #, 1)
#lcm([5, 5, 5]) #, 5)
#lcm([67, 34, 12, 3, 2]) #, 13668)
#lcm([79, 18, 7, 3, 1]) #, 9954)
lcm([10, 20, 30, 40, 50]) #, 600)
#lcm([2, 3, 5, 7, 11, 13, 17]) #, 510510)
#lcm([91, 92, 93, 94, 95]) #, 3476431140) 