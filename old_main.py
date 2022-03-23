from random import randint
import time

proizvoditelnost = (1100, 1160, 1100, 1000, 1050, 1000, 1150, 1150, 1160, 1150)
day_3 = [22500, 0, 16500, 0, 2226, 0, 4600, 12450, 0, 0]
day_4 = [14015, 16250, 0, 0, 0, 0, 5400, 3800, 0, 0]
day_5 = [8200, 8200, 10100, 0, 0, 8200, 8200, 8200, 0, 3200]
potrebnosti = [day_3, day_4, day_5]

time1 = 0
time2 = 0
spis1 = []
time_spis1 = []
spis2 = []
time_spis2 = []
tovar_spis = []
num1 = 1
num2 = 1
tovar1 = 0
tovar2 = 1
day_num = 0


class Line1():
    def proizvodstvo1():
        global num1, tovar1, time1
        ost = potrebnosti[day_num][tovar1]            
        for i in range(10000):
            main = potrebnosti[day_num][tovar1]
            x = randint(0, 24)
            if num1 != 1:
                second = (main + 100) - (proizvoditelnost[tovar1] * x)
                if second > -proizvoditelnost[tovar1]:
                    if second < ost:
                        ost = second
                        time1 = x + 1
            else:
                second = main - (proizvoditelnost[tovar1] * x)
                if second > -proizvoditelnost[tovar1]:
                    if second < ost:
                        ost = second
                        time1 = x
        spis1.append(ost)
        time_spis1.append(time1)


class Line2():
    def proizvodstvo2():
        global num2, tovar2, time2
        ost = potrebnosti[day_num][tovar2]
        for i in range(10000):
            main = potrebnosti[day_num][tovar2]
            x = randint(0, 24)
            if num2 != 1:
                second = (main + 100) - (proizvoditelnost[tovar2] * x)
                if second > -proizvoditelnost[tovar2]:
                    if second < ost:
                        ost = second
                        time2 = x + 1
            else:
                second = main - (proizvoditelnost[tovar2] * x)
                if second > -proizvoditelnost[tovar2]:
                    if second < ost:
                        ost = second
                        time2 = x
        spis2.append(ost)
        time_spis2.append(time2)


while day_num != len(potrebnosti):
    tovari = len(potrebnosti[day_num])


    while potrebnosti[day_num][tovar2] == 0 or potrebnosti[day_num][tovar1] == 0:
        if tovar1 == 9 or tovar2 == 9:
            day_num += 1
            break
        elif potrebnosti[day_num][tovar2] == 0:
            tovar2 += 1
        elif potrebnosti[day_num][tovar1] == 0:
            tovar1 += 1


    if day_num == len(potrebnosti):
        break


    if sum(time_spis1) == sum(time_spis2):
        Line1.proizvodstvo1()
        Line2.proizvodstvo2()
        tovari -= 2
        tovar_spis.append(tovar1 + 1)
        tovar_spis.append(tovar2 + 1)
        num1 += 1
        num2 += 1
    elif sum(time_spis1) < sum(time_spis2):
        tovari -= 1
        num1 += 1
        Line1.proizvodstvo1()
        tovar_spis.append(tovar1 + 1)
    elif sum(time_spis1) > sum(time_spis2):
        tovari -= 1
        num2 += 1
        Line2.proizvodstvo2()
        tovar_spis.append(tovar2 + 1)


    while tovari != 0:
        if tovar1 == 8 and day_num == 2:
            print('Tovar1 ', tovar1)
            #time.sleep(2)
        if sum(time_spis1) == sum(time_spis2):
            if tovar1 == 0:
                tovar1 = tovar2 + 1
            if tovar2 > tovar1:
                tovar1 = tovar2 + 1
            else:
                tovar2 = tovar1 + 1
            tovar1 += 1
            tovar2 += 1
            num2 += 1
            num1 += 1
            if tovar1 > 9 or tovar2 > 9:
                break
            if potrebnosti[day_num][tovar1] == 0:
                continue
            elif potrebnosti[day_num][tovar2] == 0:
                continue
            Line1.proizvodstvo1()
            Line2.proizvodstvo2()
            tovar_spis.append(tovar1 + 1)
            tovar_spis.append(tovar2 + 1)
            tovari -= 2
        elif sum(time_spis1) > sum(time_spis2):
            tovari -= 1
            tovar2 += 1
            print(tovar2)
            num2 += 1
            if tovar2 > 9 or potrebnosti[day_num][tovar2] == 0:
                continue
            Line2.proizvodstvo2()
            tovar_spis.append(tovar2 + 1)
        elif sum(time_spis1) < sum(time_spis2):
            tovari -= 1
            tovar1 = tovar2 + 1
            num1 += 1
            if potrebnosti[day_num][tovar1] == 0:
                continue
            Line1.proizvodstvo1()
            tovar_spis.append(tovar1 + 1)
            if tovar1 - tovar2 > 0:
                tovar2 += 1
    day_num += 1
    tovar1 = 0
    tovar2 = 0

    


print(tovar_spis)
print(spis1)
print(time_spis1)
print()
print(spis2)
print(time_spis2)
print()
print(max((sum(time_spis2), sum(time_spis1))) / 24)
