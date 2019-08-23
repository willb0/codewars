#Given (m,n), return the first m multiples of n
#https://www.codewars.com/kata/return-the-first-m-multiples-of-n/train/python

def multiples(m,n):
    return [n*y for y in range(1,m+1)]

#Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?
#If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".
#https://www.codewars.com/kata/exclamation-marks-series-number-17-put-the-exclamation-marks-and-question-marks-to-the-balance-are-they-balanced/train/python

def balance(left, right):
    x,y=0
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