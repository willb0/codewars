
#Given a String return a new string with opposite case and order ex("AbcD ss"==>"SS aBCd")
#https://www.codewars.com/kata/string-transformer/
def string_transformer(s):
    s=s.split(' ')
    main=''
    ret=''
    for x in range(len(s)):
        strs=''
        for y in range(len(s[x])):
            if(s[x][y].isupper()):
                strs+=s[x][y].lower()
            else:
                strs+=s[x][y].upper()
        main+=strs
        main+=' '
    ret=main.split(' ')
    ret.reverse()
    return ' '.join(ret)[1:]
