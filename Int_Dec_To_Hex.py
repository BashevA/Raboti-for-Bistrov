import sys

from Unsigned_Converts import binToHex, decToBin, binToDec

def signedDecToBin(number, bytesCount):
    if number >= 0: 
        return f"0{decToBin(number, bytesCount*8 - 1)}"
    else:
        reversed = binToDec(reverse(decToBin(-number, bytesCount*8 - 1))) + 1
        return f"1{decToBin(reversed, bytesCount*8 - 1)}"

# 11001110 -> 00110001
def reverse(bin):
    newBin = ""
    for e in bin:
        if e == "0": newBin += "1"
        else: newBin += "0"
    return newBin


if __name__ == "__main__":
    dec_num = (str(input("Введите целое  положительное десятичное число: ")))

    bin = signedDecToBin(int(dec_num), 2)
    print(bin)
    print(binToHex(bin).lstrip("0"))

