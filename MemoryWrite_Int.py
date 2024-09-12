def int_fract(dec_num, base):
    intpa = ""    
    fractpa = ""
    flag = False    
    for i in dec_num:
        if i == ",":            
            flag = True
            continue        
        if flag == False:
            intpa = intpa + i        
        else:
            fractpa = fractpa + i    
    return HexTranslate(ZeroPadding(calToBiSys(dec_num), base), dictionary)

    
dictionary = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}


def calToBiSys(dec_num):    
    flag = False
    if "-" in str(dec_num): 
        dec_num = str(dec_num[1:])  
        minus = "-"        
        flag = True
    else:        
        minus = ""
    quotient = int(dec_num)    
    remains = ""
    while quotient > 0:  
        remains = str(quotient % 2) + remains
        quotient = quotient // 2
    if flag == True:
        remains = minus + str(remains)
    else: remains = remains
    return remains


def ZeroPadding(binariNumber, base):
    if "-" in binariNumber:
        minus = True
        binariNumber = binariNumber[1:]  
    else:
        minus = False
    if int(base) > len(str(binariNumber)):
        while int(base) > len(str(binariNumber)):
            binariNumber = "0" + str(binariNumber)
    if minus == True:
        binariNumber = binariNumber[1:] 
        binariNumber = "1" + binariNumber
    else: binariNumber = binariNumber
    return binariNumber

def HexTranslate(binariNumber, dictionary):
    HexNumber = ""
    while len(str(binariNumber)) != 0:
        lenOfBinaryNumber = len(str(binariNumber))
        circle = lenOfBinaryNumber - 4
        partBinNum = str(binariNumber[circle:])
        HexNumber = dictionary[str(partBinNum)] + HexNumber
        binariNumber = str(binariNumber[:circle])
    return HexNumber


if __name__ == "__main__":    
    dec_num = (str(input("Введите целое число: ")))
    base = (str(input("Введите сколько байт в памяти: ")))
    print(int_fract(dec_num, base))




    
