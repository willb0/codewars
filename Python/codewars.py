data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
import re
def data_reverse(data):
    y=''
    x=''
    for x in data:
        y+=str(x)
    x=re.findall('........',y)
    y=x[::-1]
    return int(''.join(y)))
data_reverse(data1)
