import math


def task18(weight, pages, string, simv):
    biteWeight = weight * 8
    allSimv = pages * string * simv
    i = biteWeight / allSimv
    N = 2**i
    return int(N)

def task19(text1, text2):
    IText1 = math.log2(text1)
    IText2 = math.log2(text2)
    Difference = IText1 / IText2
    return Difference

def task20(N, I):
    i = math.log2(N)
    K = I / i
    return K


def task7(i, K):
    N = 2**i * K
    # Т.к количество банок синей и белой краски одинаково то получаем ==>
    WB = 8 + 8
    Brown = N - WB
    return Brown


def task19(H):
    N = 2**H
    return N

def task20(H):
    N = 2**H
    return N


if __name__ == "__main__":
    
    # Задание 18(Кибернетика)
    # inp18_1 = int(input("Введите общеий объём в байтах: "))
    # inp18_2 = int(input("Введите количество страниц: "))
    # inp18_3 = int(input("Введите количество строк: "))
    # inp18_4 = int(input("Введите количество символов в строке: "))
    # print( "Количество символов в алфавите составляет: ", task18(inp18_1, inp18_2, inp18_3, inp18_4))

    # Задание 19(Кибернетика)
    # inp19_1 = int(input("Введите мощность первого алфавита: "))
    # inp19_2 = int(input("Введите мощность второго алфавита: "))
    # print("Мощность алфавитов отличается в ", task19(inp19_1, inp19_2))

    # Задание 20(Кибернетика)
    # inp20_1 = int(input("Введите мощность алфавита: "))
    # inp20_2 = int(input("Введите общеий вес текста: "))
    # print("Количество символов в данном сообщении составляет: ", task20(inp20_1, inp20_2))

    # Задание 7(на разновероятностные события)
    # inp7_1 = int(input("Введите вес 1 банки белой краски: "))
    # inp7_2 = int(input("Введите количество банок синей краски: "))
    # print("Количество банок коричневой краски: ", task7(inp7_1, inp7_2))

    # Задание 19(Равновероятностные)
    # inp19_1 = int(input("Введите вес информации: "))
    # print("Количество этажей в доме составляет: ", task19(inp19_1))
    
    # Задание 20(Равновероятностные)
    # inp20_1 = int(input("Введите вес информации: "))
    # print("Количество подъездов в доме составляет: ", task20(inp20_1))
