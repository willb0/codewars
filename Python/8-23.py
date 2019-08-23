#Given (m,n), return the first m multiples of n
#https://www.codewars.com/kata/return-the-first-m-multiples-of-n/

def multiples(m,n):
    return [n*y for y in range(1,m+1)]

#Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?
#If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".
#https://www.codewars.com/kata/exclamation-marks-series-number-17-put-the-exclamation-marks-and-question-marks-to-the-balance-are-they-balanced/

def balance(left, right):
    x,y=0,0
    for q in left:
        if(q=='!'):
            x+=2
        else:
            x+=3
    for q in right:
        if(q=='!'):
            y+=2
        else:
            y+=3
    if(x>y):
        return 'Left'
    elif(x<y):
        return 'Right'
    return 'Balance'
#Return a list [x,y] in which x is the number of iterations 
#to reach a point in which the difference of the expansion 
# of PI/4 and PI/4 is less than decplace, showing accuracy to 
#the decplace place, and y is the value of the PI/4 series expansion
# at the end of the iterations
#ex: iter_pi(.001)==>[1000, 3.1405] 
#It takes 100 iterations of the PI/4 series expansion to reach .001 
#place accuracy of PI
#https://www.codewars.com/kata/pi-approximation/
import math
def iter_pi(decplace):
    #Not sure why [:len(str(decplace))+11] works instead of +10 
    #to account for the rounding at the end the rounding 
    pi=(float(str(math.pi)[:len(str(decplace))+11]))
    x=1
    y=0
    itercount=0
    bool=True
    #loop that represents the alternating PI/4 expansion series 
    while(abs(y*4-pi)>decplace):
        if(bool):
            y+=(1/x)
            bool=False
        else:
            y-=(1/x)
            bool=True
        x+=2
        itercount+=1
    return [itercount,round(y*4,10)]