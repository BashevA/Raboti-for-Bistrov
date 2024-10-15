from Unsigned_Converts import hexToBin, binToDec


def signedHexToBin(hex, bytesCount):
    binNum = hexToBin(hex).rjust(bytesCount*8, "0")
    negative = binNum[0] == "1"
    power = binToDec(binNum[2:8])
    
    # Извлекаем данные о числе
    mantisa = binNum[8:]
    decPart = binToDec(mantisa[:power]) # 001
    floatPart = int(floatPartToInt(mantisa[power:])) # 10101
    if negative:
        decNum = "-" + str(decPart) + "," + str(floatPart)  
    else:
        decNum = str(decPart) + "," + str(floatPart)
    return decNum

def floatPartToInt(fracPa):
    lenOfFractPa = len(fracPa)
    sum = 0
    index = 0
    cor = -1
    result = 0
    while index < lenOfFractPa:
        number = int(fracPa[index])
        sum = number * (2**(cor))
        index +=1
        cor-=1
        result = result + sum
    result = str(result)
    return result[2:]

# 4796

    # 515.124

    # 515 -A> 10100101
    # 124 -B> 101010010
    # 10100101.101010010
    
    # 10100101 ~A> 515
    # 101010010 ~B> 124
    # float(f"{515}.{124}")


# {negative}1{ilen[6]} {int part[ilen]}{float part[len - ilen]}
if __name__ == "__main__":
    print(signedHexToBin(input(), 4))