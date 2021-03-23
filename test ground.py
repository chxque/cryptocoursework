letterFrequencyArray = (['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z'],
                        [0.1202,0.91,0.812,0.768,0.731,0.695,0.628,0.602,0.592,0.432,0.398,0.288,0.271,0.261,0.230,0.211,0.209,0.203,0.182,0.149,0.111,0.069,0.017,0.011,0.01,0.007])
n=26

def twoDBubble(array):
    for i in range(len(array[1])):
        for j in range(len(array[1])-1):
            if (array[1][j] < array[1][j+1]):
                array[0][j],array[0][j+1] = array[0][j+1],array[0][j]
                array[1][j],array[1][j+1] = array[1][j+1],array[1][j]
    return array
                
def simult(m1,m2,c1,c2):
    m1 = ord(m1) - ord('A')
    m2 = ord(m2) - ord('A')
    c1 = ord(c1) - ord('A')
    c2 = ord(c2) - ord('A')
    n=26
    ct = (c1 - c2)%n
    mt = (m1 - m2)%n
    mti, gcd = eEuclidean(mt)
    if not gcd == 0:
        a = (ct/mt)%n
    else:
        a = (ct*mti)%n

    b=(c1-(a*(m1)))%n

    ai, gcd = eEuclidean(a)
        
    return a,b,gcd


def eEuclidean(a):
    x,y,previousX,previousY = 1,a,0,n
    while (y):
        quotient = previousY // y
        previousX, x = x, (previousX - quotient*x)
        previousY, y = y, (previousY - quotient*y)

    return previousX,previousY

print(simult('C','A','S','I'))

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
            t = chr(int(t))
        transformedtext += t    
    return transformedtext

def freqAnalysis(cipherText):
    message = cipherText.upper()
    cipherFrequency=([],[])
    tempArr = []
    cipherText = ''.join(cipherText.split())
    cipherText.upper()
    cipherTemp=''
    for i in range (0,len(cipherText)):
        if (((ord(cipherText[i])) >= ord('A')) and ((ord(cipherText[i])) <= ord('Z'))):
            cipherTemp += cipherText[i]
            tempArr.append((sorted(cipherText))[i])
    cipherText=cipherTemp
    tempArr2=([],[])
    for i in range (0,len(cipherText)):
        if i == 0:
            last=tempArr[i]
            tempArr2[0].append(last)
            tempArr2[1].append(1)
            current = 0
        else:
            last=tempArr[i-1]
            if not(tempArr[i] == last):
                tempArr2[0].append(tempArr[i])
                tempArr2[1].append(1)
                current += 1
            else:
                tempArr2[1][current] += 1
                
    tempArr2 = twoDBubble(tempArr2)

    for i in range(len(tempArr2[1])):
        tempArr2[1][i] = ("%.4f" % (tempArr2[1][i] / len(cipherText)))
    
    print (tempArr2[0])
    print (tempArr2[1])

    tempArr3 = []
    tempArr4 = ([],[])
    tempArr5 = ([],[])
    tempArr6 = ([],[],[])
    tempArr7 = ([],[])

    for i in range(len(tempArr2[0])):
        for j in range(len(tempArr2[0])):
            if not((tempArr2[0][i] == tempArr2[0][j])):
                tempArr4[0].append(tempArr2[0][j] + ',' + tempArr2[0][i])
                tempArr4[1].append(float(tempArr2[1][j]) + float(tempArr2[1][i]))


    for i in range(len(letterFrequencyArray[0])):
        for j in range(len(letterFrequencyArray[0])):
            if not((letterFrequencyArray[0][i] == letterFrequencyArray[0][j])):
                tempArr5[0].append(letterFrequencyArray[0][j] + ',' + letterFrequencyArray[0][i])
                tempArr5[1].append(float(letterFrequencyArray[1][j]) + float(letterFrequencyArray[1][i]))

    for i in range(len(tempArr4[0])):
        for j in range(len(tempArr5[0])):
            if not((tempArr4[0][i] == tempArr5[0][j])):      
                if (float(tempArr4[1][i]) + float(tempArr5[1][j]))/4 > 0.0:
                    probability=float(tempArr4[1][i]) + float(tempArr5[1][j])
                    tempVar1, tempVar2 = tempArr4[0][i].split(','), tempArr5[0][j].split(',')
                    a,b,gcd = simult(tempVar1[0],tempVar1[1],tempVar2[0],tempVar2[1])
                    if gcd == 1.0:
                        currentAB=(str(a)+','+str(b))
                        if not(currentAB in tempArr7[0]):
                            tempArr7[0].append(currentAB)
                            tempArr7[1].append(probability)
                            tempArr6[0].append(tempArr4[0][i] + ',' + tempArr5[0][j])
                            tempArr6[1].append(probability)
                            tempArr6[2].append(tempVar1[0] + tempVar1[1] + tempVar2[0] + tempVar2[1])
                    
                    
    print('accumulated',len(tempArr4[0]),len(tempArr5[0]),len(tempArr6[0]))                           
    tempArr6 = twoDBubble(tempArr6)
    for i in range(len(tempArr6[0])):
        a,b,gcd = simult(tempArr6[2][i][0],tempArr6[2][i][1],tempArr6[2][i][2],tempArr6[2][i][3])
        print((decrypt(a,b,message)),tempArr6[1][i],'\n')

freqAnalysis('SIV OC MCZ I FAMSRIQF WV SRIZ?')
                
        
        
