from collections import Counter
def find_it(seq):
    s=Counter(seq)
    for x in seq:
        if s[x]%2!=0:
            return x
        ##print(x,s[x])
        
    return None
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))