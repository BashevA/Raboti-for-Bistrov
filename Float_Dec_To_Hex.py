import sys

from Unsigned_Converts import decToBin, binToHex

def signedFloatToBin(dec_num, bytesCount):
    minus = dec_num[0] == "-"
    if minus:
        dec_num = dec_num[1:]

    # Разделяем число
    s = dec_num.split(",") 

    if len(s) == 2: # "2,22" -> ["2", "22"] (длина == 2)
        (int_part, fract_part) = s
    elif len(s) == 1: # "51" -> ["51"] (длина < 2)
        (int_part, fract_part) = (s[0], "0")
    else: # ("" -> []) ИЛИ ("31,51,234" -> ["31", "41", "234"]) и т. д.
        raise ValueError("Неправильный формат числа")

    IntPart = decToBin(int_part)

    # Сколько байтов осталось для вещественной части
    remainBytes = (bytesCount - 1) * 8 - len(IntPart)

    if remainBytes < 0:
        raise Exception("Число слишком большое")

    floatPart = floatPartToBin(fract_part, remainBytes)
    
    
    # Длина целой части в бинарном формате
    power = decToBin(len(IntPart))

    #        {негативность числа}{ коэфицент смещения }{ целая часть + дробная часть }
    return f"{1 if minus else 0 }{int(power) + 1000000}{str(IntPart) + str(floatPart)}"


# Преобразует вещественную часть числа в двоичную
# с длинной в битах bitLen
def floatPartToBin(fracPart, bitLen): 
    result = ""
    floatFracPart = float("0." + fracPart) 
    
    for i in range(bitLen): 
        floatFracPart = floatFracPart * 2
        
        if floatFracPart >= 1:
            result += "1"
            floatFracPart -= 1
        else:
            result += "0"

        # Автоматически останавливаться, если начались бесконечные нули
        # if floatFracPart == 0:
        #    break
    return result

if __name__ == "__main__":    
    dec_num = input("Введите целое десятичное число: ")
    binary = signedFloatToBin(dec_num, 4)
    hexNum = binToHex(binary)
    print(binary)
    print(hexNum)

