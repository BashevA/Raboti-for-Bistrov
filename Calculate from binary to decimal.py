def int_fract(dec_num):
    intPa = ""
    fracPa = ""
    flag = False
    for i in dec_num:
        if i == ",":
            flag = True
            continue
        if flag == False:
            intPa = intPa + i
        else:
            fracPa = fracPa + i
    # if flag == False:
    #     fracPa = 0
    return str(intConv(intPa)) + "," + str(fractPa(fracPa))

def intConv(intPa):
    lenOfIntPa = len(intPa)
    sum = 0
    index = 0
    cor = 1
    result = 0
    while index < lenOfIntPa:
        number = int(intPa[index])
        sum = number * (2**(lenOfIntPa - cor))
        index +=1
        cor +=1
        result = result + sum    
    return result

def fractPa(fracPa):
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


if __name__ == "__main__":
    dec_num = str(input("Введите двоичное число: "))
    print(int_fract(dec_num))





    

    



