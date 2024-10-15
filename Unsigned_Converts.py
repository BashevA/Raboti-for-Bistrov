# Все преобразования беззнаковых целочисленных значений


hexToBinDict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010", 
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

binToHexDict = {
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

def decToBin(number, bitsCount = 0):
    quotient = int(number)    
    remains = ""
    while quotient > 0:  
        remains = str(quotient % 2) + remains
        quotient = quotient // 2
    if bitsCount == 0:
        return remains
    else:
        # rjust(10101, 8) -> 00010101 
        return remains.rjust(bitsCount, "0") 

def binToDec(bin):
    lenOfIntPa = len(bin)
    sum = 0
    index = 0
    cor = 1
    result = 0
    while index < lenOfIntPa:
        number = int(bin[index])
        sum = number * (2**(lenOfIntPa - cor))
        index += 1
        cor += 1
        result = result + sum    
    return result

def binToHex(bin):
    hex = ""
    if len(bin) % 4 != 0:
        bin = "0" * (4 - (len(bin)%4)) + bin
    
    for i in range(0, len(bin), 4):
        binPart = bin[i:i+4]
        hex += binToHexDict[binPart]
    return hex


def hexToBin(hexValue):
    binStr = ""
    for i in hexValue:
        binStr += hexToBinDict[i]
    return binStr