from Unsigned_Converts import binToDec, binToHex, decToBin, hexToBin

import Int_Dec_To_Hex

# v -> reverse(v) -> v+=1 -> hex(v)
# unhex(v) -> v-=1 -> reverse(v) -> v

def signedHexToDec(hexNum, bytesCount):
    bin = hexToBin(hexNum).rjust(bytesCount, "0")
    negative = bin[0] == "1"
    if negative:
        value = bin[1:]
        value = decToBin((binToDec(value) - 1))
        value = Int_Dec_To_Hex.reverse(value)
        return -binToDec(value)
    else:
        return binToDec(bin)

if __name__ == "__main__":
    print(signedHexToDec(input(), 2))

