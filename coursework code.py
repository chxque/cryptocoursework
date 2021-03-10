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
    inverseA = inverse(a)
    message = ''
    for c in cipher:
        c = c.upper()
        if not (c.isspace()):
            c = ord(c) - ord('A')
            if ((c >= 0) and (c <= 25)):               
                c = (inverseA*(c-b) % n) + ord('A')
            else:
                c += ord('A')
            c = chr(c)
        message += c    
    return message

def encrypt(a,b,message):
    cipher = ''
    for m in message:
        m = m.upper()
        if not (m.isspace()):
            m = ord(m) - ord('A')
            if ((m >= 0) and (m <= 25)):               
                m = (((a*m)+b) % n) + ord('A')
            else:
                m += ord('A')
            m = chr(m)
        cipher += m    
    return cipher
    

print(decrypt(5,8,'SIV OC MCZ I FAMSRIQF WV SRIZ?'))
print(encrypt(5,8,'CAN WE GET A POGCHAMP IN CHAT?'))

