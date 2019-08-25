##long description so goinf to summarize:
#a building has a pile of n cubes, with the bottom cube having n^3
#volume, the next cube up having (n-1)^3 volume, and et cetera until 
#the top cube which is 1^3. Given the total volume of the building,
#return the integer n that as the bottom cube, will lead to a volume m
#if there is no such integer, return -1
#https://www.codewars.com/kata/5592e3bd57b64d00f3000047
import math
def find_nb(n):
    x=0
    y=0
    while x!=n:
        x+=(y)**3
        y+=1
        if(x>n):
            return -1
    return(y-1)

def what_is_the_time(timeinmirror):
    t=int(timeinmirror.split(':')[0])*60+int(timeinmirror.split(':')[1])
    q=720+(720-t)
    if q>779:
        q=q-720
    return '{:02}:{:02}'.format((int(round(q/60))),int(q%60))
print(what_is_the_time('11:59'))
