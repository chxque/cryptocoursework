import argparse

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--e','--encrypt', action='store_true')
    parser.add_argument('--d','--decrypt', action='store_true')  
    parser.add_argument('-k','-key')
    parser.add_argument('-m','-message',default='GFUFPSXCNKUZBSFAHBCZUQJL', nargs='+')
    parser.add_argument('--c','--crack',action='store_true')
    parser.add_argument('-mp','-maximum probability', default=0.08) 
    args = parser.parse_args()
    args.m = ' '.join(args.m)
    return args.k, args.e, args.d, (args.m).upper(), args.c, float(args.mp)

letterFrequencyArray = (['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z'],
                        [0.1202,0.091,0.0812,0.0768,0.0731,0.0695,0.0628,0.0602,0.0592,0.0432,0.0398,0.0288,0.0271,0.0261,0.0230,0.0211,0.0209,0.0203,0.0182,0.0149,0.0111,0.0069,0.0017,0.0011,0.001,0.0007])


def twoDimensionalBubble(array):
    for i in range(len(array[0])):
        for j in range(len(array[0])-1):
            if (array[1][j] > array[1][j+1]):
                for k in range(len(array)):
                    array[k][j],array[k][j+1] = array[k][j+1],array[k][j]

    return array

def egcd(a,b):
    x,y,previousX,previousY = 0,1,1,0
    while (a != 0):
        quotient, r = b//a, b%a
        m,n = x-quotient*previousX,y-quotient*previousY
        b,a,x,y,previousX,previousY = a,r,previousX,previousY,m,n
    return b,x%26
        

def plaintext(m1,m2,c1,c2):
    m1 = ord(m1) - ord('A')
    m2 = ord(m2) - ord('A')
    c1 = ord(c1) - ord('A')
    c2 = ord(c2) - ord('A')
    d = (m1 - m2)%26
    gcd,dInv = egcd(d,26)
    if (gcd == 1):
        a = (dInv*(c1-c2))%26
    else:
        a = ((c1-c2)//d)%26

    b = (c1 - (a*m1))%26
    gcd = egcd(a,26)[0]
    
    return a,b,gcd

def decrypt(a,b,cipher):
    execute = "(a*(t-b) % 26) + ord('A')"
    message = parse(egcd(a,26)[1],b,cipher,execute)
    return message

def encrypt(a,b,message):
    execute = "(((a*t)+b) % 26) + ord('A')"
    cipher = parse(a,b,message,execute)
    return cipher

def parse(a,b,text,execute):
    if a == '':
        return
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

def frequencyAnalysisCrack(cipherText,probabilityMin):
    crackText = [],[]
    
    for i in (''.join(cipherText.split())):
        if (((ord(i)) >= ord('A')) and ((ord(i)) <= ord('Z'))):
            if (i not in crackText[0]):
                crackText[0].append(i)
                crackText[1].append(1)
            else:
                crackText[1][crackText[0].index(i)] += 1

    twoDimensionalBubble(crackText)
    TempCrackText = [],[]
    for i in range(2):
        TempCrackText[1].append(float("%.4f" % (crackText[1][i-len(crackText)] / len(crackText[0]))))
        TempCrackText[0].append(crackText[0][i-len(crackText)])
     
    
    crackText = TempCrackText
    print(crackText)
    del TempCrackText
    possibleKnownCombinations = [],[],[]
    for i in range(len(letterFrequencyArray[0])):
        for j in range(len(letterFrequencyArray[0])):
            probability = (letterFrequencyArray[1][i] + letterFrequencyArray[1][j] + crackText[1][0] + crackText[1][1]) / 4
            if not(letterFrequencyArray[0][i] == letterFrequencyArray[0][j]) and probability >= probabilityMin:
                currentCombination = [letterFrequencyArray[0][i],letterFrequencyArray[0][j],crackText[0][0],crackText[0][1]]
                combinationInfo = plaintext(currentCombination[0],currentCombination[1],currentCombination[2],currentCombination[3])
                if combinationInfo[2] == 1:
                    possibleKnownCombinations[0].append(currentCombination)
                    possibleKnownCombinations[1].append(probability)
                    possibleKnownCombinations[2].append(combinationInfo)

    possibleKnownCombinations = twoDimensionalBubble(possibleKnownCombinations)

    for i in range(len(possibleKnownCombinations[0])):
        combinationInfo = possibleKnownCombinations[2][i]
        print(decrypt(combinationInfo[0],combinationInfo[1],cipherText),'\n Key:   A = ',combinationInfo[0],' B = ',combinationInfo[1],' Probability = ',possibleKnownCombinations[1][i])

    print('Number of possible combinations: ',len(possibleKnownCombinations[0]))
    
            
    

key, encryptBool, decryptBool, messageText, crackBool, probabilityMin = get_args()

if(crackBool):
    print(messageText)
    frequencyAnalysisCrack(messageText,probabilityMin)
elif encryptBool or decryptBool:
    a,b=[int(x) for x in key.split(',')]
    if(encryptBool):
        print(encrypt(a,b,messageText))

    elif(decryptBool):
        print(decrypt(a,b,messageText))
else:
    print('No function selected')
