# cryptocoursework
# Affine Cipher Coursework
*Philip Blamire (P2538576)*

*Nicky Basi (P2535513)*

*Marti Borisov (P2535513)*

*Osama Mohammed A Alzahrani (P2524209)*

------------

#### To use the program:
> *python3 needed*

run from command line or terminal, I'm using macOS so I run:
`% python3 Affine\ Cipher\ Tools.py <arguments>`

There are multiple optional arguments that can be run:
     --e / --encrypt - a boolean flag that tells the program you are encrypting a string
    --d / -decrypt - a boolean flag that tells the program you are decrypting a string
    --c / -crack - a boolean flag that tells the program you are cracking a string
    -k / -key - used: -k <a,b>, specifies your key for encrypting or decrypting, if --d is specified but no key is given, the program will crack the key
    -m / -message - used: -m <'message'> specifies the string to en/decrypt / crack
    -mp - used: -mp <0.000 - 1.000>, specifies the minimum probability of a key pair to be shown, default is 0.08


> cracking lists answers from lowest probability to highest

------------

## here are some examples for running the program
### Cracking
`python3 Affine\ Cipher\ Tools.py --c -mp 0.1 -m 'GFUFPSXCNKUZBSFAHBCZUQJL'`
--c : crack enabled 
-mp 0.1 : minimum probability = 0.1
--m 'GFUFPSXCNKUZBSFAHBCZUQJL' : sets text to be cracked
#####gives the output:
![](https://raw.githubusercontent.com/chxque/cryptocoursework/main/images/Screenshot%202021-03-25%20at%2018.48.10.png)

### decrypting
`% python3 Affine\ Cipher\ Tools.py --d -k 25,16 -m 'OIBJMZXMTXNMOZSBXMNIDXCBFQIDXMTX'`
--d : decrypting with key enabled
-k 25,16 : sets a to 25, b to 16
-m : sets text to be decrypted
gives the output:
![](https://raw.githubusercontent.com/chxque/cryptocoursework/main/images/Screenshot%202021-03-25%20at%2019.17.22.png)

### Encrypting
`% python3 Affine\ Cipher\ Tools.py --e -k 19,9 -m 'PLAINTEXTISENCRYPTEDINTOCIPHERTEXT'
`
--e : encrypting enabled
-k 19,9 : sets a to 19, b to 9
-m : sets text to be encrypted
gives the output:
![](https://raw.githubusercontent.com/chxque/cryptocoursework/main/images/Screenshot%202021-03-25%20at%2019.19.48.png)

## Known issues
#### for some reason, running using defaults in the python idle kind of does not preserve spaces
Well, technically it doesn, but it adds spaces inbetween each character, so a space would be invisible
![](https://raw.githubusercontent.com/chxque/cryptocoursework/main/images/Screenshot%202021-03-25%20at%2018.49.31.png)

#### not really an issue, but our specific cipher text isnt high up on the crack list
Just because it is  too short for frequency analysis to be accurate enough.
here are some of the other teams cipher texts:
> ![](https://raw.githubusercontent.com/chxque/cryptocoursework/main/images/MicrosoftTeams-image.png)

> ![](https://raw.githubusercontent.com/chxque/cryptocoursework/main/images/MicrosoftTeams-image2.png)
