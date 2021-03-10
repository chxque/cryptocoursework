n = 26

def eEuclidean(a):
    x,y,previousX,previousY = 1,a,0,n
    while (y):
        quotient = previousY // y
        previousX, x = x, (previousX - quotient*x)
        previousY, y = y, (previousY - quotient*y)

    return previousX,previousY

def inverse(a):
    x,gcd = eEuclidean(a)
    if not (gcd == 1):
        return null
    else:
        return(x+n)

def decrypt(a,b,cipher):
    message = ''
    for c in cipher:
        c = c.upper()
        if not (c.isspace()):
            c = ord(c) - ord('A')
            if ((c >= 0) and (c <= 25)):               
                c = (inverse(a)*(c-b) % n) + ord('A')
            else:
                c += ord('A')
            c = chr(c)
        message += c    
    return message

print(decrypt(5,8,'siv oc mcz i famsriqf wv sriz?'))
