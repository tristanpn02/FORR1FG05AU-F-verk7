##########################
# Tristan Pétur Andersen #
# 27 September 2018      #
# Æfingaverkefni 7       #
##########################

import os
from os import system


#Finna út hvaða lið notandi vill nota og opna það
def main():
    os.system('cls')
    lidur = int(input('Sláðu in númer á lið: '))
    
    if lidur == 1:
        print('-' * 20)
        lidur1()
        input()
    elif lidur == 2:
        print('-' * 20)
        lidur2()
        input()
    elif lidur == 3:
        print('-' * 20)
        lidur3()
        input()
    elif lidur == 4:
        print('-' * 20)
        lidur4()
        input()
    elif lidur == 5:
        print('-' * 20)
        lidur5()
        input()
    elif lidur == 6:
        print('-' * 20)
        lidur6()
        input()
    elif lidur == 7:
        print('-' * 20)
        lidur7()
        input()
    elif lidur == 8:
        print('-' * 20)
        lidur8()
        input()

    main()
    
#Liður 1:
def lidur1():
    os.system('cls')
    
    counter = 20
    while counter <=40:
        print(counter, end=" ")
        counter = counter + 2

#Liður 2

def lidur2():
    os.system('cls')
    
    res = 0
    counter = 15
    while counter <= 345:
        res = res + counter
        counter = counter + 2
    print(res)
    
#Liður 3
def lidur3():
    os.system('cls')
    
    desNum = int(input("Sláðu inn tölu sem er lærri en 100: "))
    
    if desNum > 100:
        input("Þessi tala er ekki lærri en 100! [ENTER]")
        lidur3()
        
    while desNum <= 100:
        print(desNum, end=" ")
        desNum = desNum + 1
        
#Liður 4
def lidur4():
    os.system('cls')
    
    desNum = int(input("Sláðu inn tölu sem er stærri en 100: "))
    
    if desNum < 100:
        input("Þessi tala er ekki stærri en 100! [ENTER]")
        lidur4()
    
    while desNum >= 100:
        print(desNum, end=" ")
        desNum = desNum - 1
        
#Liður 5
def lidur5():
    os.system('cls')
    
    desNum = int(input('Sláðu inn tölu: '))
    res = desNum % 9
    amountNum = 0
    
    desNum9 = desNum
    if res == 0:
        while desNum9 > 0:
            desNum9 = desNum9 - 9
            amountNum = amountNum + 1
            
        print("9 gengur upp í töluna", amountNum, "sinnum.")
        
        
    res = desNum % 5
    amountNum = 0
    
    if res == 0:
        while desNum > 0:
            desNum = desNum - 5
            amountNum = amountNum + 1
        print("5 gengur upp í töluna", amountNum, "sinnum.")
        
#Liður 6
def lidur6():
    os.system('cls')
    
    floatNum1 = float(input("Sláðu inn kommutölu (1/2): "))
    floatNum2 = float(input("Sláðu inn kommutölu (2/2): "))
    
    res = floatNum1 / floatNum2
    
    print("%.5f" % res)
    
#Liður 7
def lidur7():
    os.system('cls')
    
    res = 0
    
    numList = []
    
    while res<1000:
        if res%15==0 and res%18==0:
            numList.append(res)
        res = res + 1
    print("15 og 18 ganga upp í", numList)
    
#Liður 8
def lidur8():
    os.system('cls')
    
    textNum = 1
    text = "barbara"
    
    while textNum < 6:
        print(text)
        textNum = textNum + 1
        text = text + " barbara"
    
main()