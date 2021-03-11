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
    execute = "(a*(t-b) % n) + ord('A')"
    message = parse(inverse(a),b,cipher,execute)
    return message

def encrypt(a,b,message):
    execute = "(((a*t)+b) % n) + ord('A')"
    cipher = parse(a,b,message,execute)
    return cipher

def parse(a,b,text,execute):
    transformedtext = ''
    for t in text:
        t = t.upper()
        if not (t.isspace()):
            t = ord(t) - ord('A')
            if ((t >= 0) and (t <= 25)):
                t = eval(execute)
            else:
                t += ord('A')
            t = chr(t)
        transformedtext += t    
    return transformedtext
    

print(decrypt(5,8,'SIV OC MCZ I FAMSRIQF WV SRIZ?'))
print(encrypt(5,8,'CAN WE GET A POGCHAMP IN CHAT?'))
