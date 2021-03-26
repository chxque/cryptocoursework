import argparse

def get_args(): #defining user arguments for CLI 
    parser=argparse.ArgumentParser() 
    parser.add_argument('--e','--encrypt', action='store_true')
    parser.add_argument('--d','--decrypt', action='store_true')  
    parser.add_argument('-k','-key')
    parser.add_argument('-m','-message',default='GFUFPSXCNKUZBSFAHBCZUQJL', nargs='+')
    parser.add_argument('--c','--crack',action='store_true')
    parser.add_argument('-mp', default=0.08) 
    args = parser.parse_args()
    args.m = ' '.join(args.m)
    return args.k, args.e, args.d, (args.m).upper(), args.c, float(args.mp)

#defining the bost to least commonly used letters, as well as their probability of being used in an english sentence at any point.
letterFrequencyArray = (['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z'],
                        [0.1202,0.091,0.0812,0.0768,0.0731,0.0695,0.0628,0.0602,0.0592,0.0432,0.0398,0.0288,0.0271,0.0261,0.0230,0.0211,0.0209,0.0203,0.0182,0.0149,0.0111,0.0069,0.0017,0.0011,0.001,0.0007])


#this is just an extended bubble sort, that sorts collumns, not just single array items, and stores them least to highest probability
def twoDimensionalBubble(array):
    for i in range(len(array[0])):
        for j in range(len(array[0])-1):
            if (array[1][j] > array[1][j+1]):
                for k in range(len(array)):
                    array[k][j],array[k][j+1] = array[k][j+1],array[k][j]

    return array

#this is the extended euclidean algorithm, takes a, the number to be inversed, and b, the modulus range
def egcd(a,b):
    x,y,previousX,previousY = 0,1,1,0
    while (a != 0): 
        quotient, r = b//a, b%a
        m,n = x-quotient*previousX,y-quotient*previousY
        b,a,x,y,previousX,previousY = a,r,previousX,previousY,m,n
    return b,x%26 # returns b (the gcd) and x mod 26, our inverse of the given aa
        


#algorithm to find the a and b of a key based on 2 'known' plain text characters and their corresponding ciphertext characters.
#accepts message 1, message 2 (the known plaintext characters) and cipher 1 and cipher 2, the corresponding ciphertext characters
def plaintext(m1,m2,c1,c2):
    m1 = ord(m1) - ord('A')
    m2 = ord(m2) - ord('A')
    c1 = ord(c1) - ord('A')
    c2 = ord(c2) - ord('A') #parsing the inputted characters to their value as 0-25
    d = (m1 - m2)%26
    gcd,dInv = egcd(d,26)
    if (gcd == 1):
        a = (dInv*(c1-c2))%26 #this is the algorithm of using a simultaneous equation to find a
    else:
        a = ((c1-c2)//d)%26 #this catches an edge case where m1-m2 isnt able to be inversed, dont touch

    b = (c1 - (a*m1))%26 #just calculates b based on the rest of our equation
    gcd = egcd(a,26)[0] # calculates the gcd of our calculated a, required to verify the letter combination is valid
    
    return a,b,gcd

def decrypt(a,b,cipher):
    execute = "(a*(t-b) % 26) + ord('A')" #setting the algorithm used in parse() to the decryption algorithm.
    message = parse(egcd(a,26)[1],b,cipher,execute) 
    return message

def encrypt(a,b,message):
    execute = "(((a*t)+b) % 26) + ord('A')" #setting the algorithm used in parse() to the encryption algorithm
    cipher = parse(a,b,message,execute)
    return cipher

#parses each character into an iterable state, and performs the algorithms provided by the function that called this function
def parse(a,b,text,execute):
    if a == '': #basic check to avoid errors
        return
    transformedtext = '' #initialising the string of the transformed text
    for t in text:
        t = t.upper() #ensuring the characters are fully capitalised
        if not (t.isspace()): #conserves spaces
            t = ord(t) - ord('A') #converts A-Z into 0-25 for algorithm
            if ((t >= 0) and (t <= 25)): #ensures a symbol isnt being encoded
                t = eval(execute) #executes the algorithm specified in the function that called parse() on current character
            else:
                t += ord('A') #if the current character was a symbol, or not A-Z, returns it back to how it was before to conserve
            t = chr(int(t)) #converts back to characters
        transformedtext += t    #appends the current character to the transformed text string
    return transformedtext

#weighted cracking algorithm using basic frequency analysis
def frequencyAnalysisCrack(cipherText,probabilityMin):
    crackText = [],[] #initialising a 2d array that stores each character in [0], 
    #and either the number of instances of that character, or the probability of that character in [1], depending on where you check
    
    #loop for populating the crackText array
    for i in (''.join(cipherText.split())):
        if (((ord(i)) >= ord('A')) and ((ord(i)) <= ord('Z'))):
            if (i not in crackText[0]): #if the current character isnt already in crackText[0], append it, nd append the value 1, to start the count of its use
                crackText[0].append(i)
                crackText[1].append(1)
            else: #if the character is already in the array, add 1 to its use count
                crackText[1][crackText[0].index(i)] += 1

    twoDimensionalBubble(crackText) #sort the array by least used to most used
    tempCrackText = [],[] #initialising a temporary array, kind of hacky, but python doesnt allow us to do this natively
    #this loop grabs the 2 most used characters for crackText (the last two in the list), as well as their corresponding probabilities, and places them in tempCrackText
    for i in range(2):
        tempCrackText[1].append(float("%.4f" % (crackText[1][i-len(crackText)] / len(crackText[0])))) #calculating and appending the probability of this character being used
        tempCrackText[0].append(crackText[0][i-len(crackText)]) #appending the character
     
    
    crackText = tempCrackText 
    del tempCrackText #deletign the temporary array from memory
    
    possibleKnownCombinations = [],[],[] #initialising a 2d array, which will contain character combinations in [0], their probability in [1], and the corresponding keys in [2]
    for i in range(len(letterFrequencyArray[0])):
        for j in range(len(letterFrequencyArray[0])): 
            probability = (letterFrequencyArray[1][i] + letterFrequencyArray[1][j] + crackText[1][0] + crackText[1][1]) / 4 #calculating the probability
            if not(letterFrequencyArray[0][i] == letterFrequencyArray[0][j]) and probability >= probabilityMin: #ensuring the two 'known' plaintexts arent the same, as thats impossible and a waste of computing
                currentCombination = [letterFrequencyArray[0][i],letterFrequencyArray[0][j],crackText[0][0],crackText[0][1]] # temporary array just to make it easier to read contains the current m1,m2,c1,c2
                combinationInfo = plaintext(currentCombination[0],currentCombination[1],currentCombination[2],currentCombination[3]) #  calculating the a and b keys, and the gcd of the a key of the current combination
                if combinationInfo[2] == 1: #ensuring the key is valid
                    possibleKnownCombinations[0].append(currentCombination)
                    possibleKnownCombinations[1].append(probability)
                    possibleKnownCombinations[2].append(combinationInfo) #appending the new possible combination to the array
    del combinationInfo
    del currentCombination #memory housekeeping
    possibleKnownCombinations = twoDimensionalBubble(possibleKnownCombinations) #sorting the array from lowest to highest probability

    for i in range(len(possibleKnownCombinations[0])): #loop to iterate through and print the possible key combinations, from least to highest probability
        combinationInfo = possibleKnownCombinations[2][i]
        print(decrypt(combinationInfo[0],combinationInfo[1],cipherText),'\n Key:   A = ',combinationInfo[0],' B = ',combinationInfo[1],' Probability = ',possibleKnownCombinations[1][i])
        del combinationInfo #more memory housekeeping
        
    print('Number of possible combinations: ',len(possibleKnownCombinations[0]))
    del possibleKnownCombinations
    
            
    

key, encryptBool, decryptBool, messageText, crackBool, probabilityMin = get_args() #call get_args to get user inputted arguments from cli

#logic based on the arguments given
#if the user enables cracking, crack the text, ignore all other enabled functions
#if not, either crack or decrypt
#if nothing was enabled, quit
if(crackBool):
    print(messageText)
    frequencyAnalysisCrack(messageText,probabilityMin)
elif encryptBool or decryptBool:
    a,b=[int(x) for x in key.split(',')] #split the key string ('a,b') into a list ([a,b])
    if(encryptBool):
        print(encrypt(a,b,messageText))

    elif(decryptBool):
        print(decrypt(a,b,messageText))
else:
    print('No function selected')
