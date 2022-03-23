from random import randint


proizvoditelnost = (1100, 1160, 1100, 1000, 1050, 1000, 1150, 1150, 1160, 1150)
day_3 = [22500, 0, 16500, 0, 2226, 0, 4600, 12450, 0, 0]
day_4 = [14015, 16250, 0, 0, 0, 0, 5400, 3800, 0, 0]
day_5 = [8200, 8200, 10100, 0, 0, 8200, 8200, 8200, 0, 3200]
potrebnosti = [day_3, day_4, day_5]
#Если прокопировать day_5 и запустить с их учётом, не срабатывает 10 производство! Нужно фиксить

day_num = 0
num = 1
tovar_spis = []
time_spis1 = []
time_spis2 = []
tovar1 = 0
tovar2 = 1


def proizvodstvo(num, tovar):
    ost = potrebnosti[day_num][tovar]
    for i in range(10000):
        main = potrebnosti[day_num][tovar]
        x = randint(0, 24)
        if num != 1:
            second = (main + 100) - (proizvoditelnost[tovar] * x)
            if second > -proizvoditelnost[tovar]:
                if second < ost:
                    ost = second
                    time = x + 1
        else:
            second = main - (proizvoditelnost[tovar] * x)
            if second > -proizvoditelnost[tovar]:
                if second < ost:
                    ost = second
                    time = x
    return (ost, time)

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
        time_spis1.append(proizvodstvo(num, tovar1)[1])
        time_spis2.append(proizvodstvo(num, tovar2)[1])
        tovari -= 2
        tovar_spis.append(tovar1 + 1)
        tovar_spis.append(tovar2 + 1)
        num += 1
    elif sum(time_spis1) < sum(time_spis2):
        tovari -= 1
        num += 1
        time_spis1.append(proizvodstvo(num, tovar1)[1])
        tovar_spis.append(tovar1 + 1)
    elif sum(time_spis1) > sum(time_spis2):
        tovari -= 1
        num += 1
        time_spis2.append(proizvodstvo(num, tovar2)[1])
        tovar_spis.append(tovar2 + 1)

    while tovari != 0:
        if sum(time_spis1) == sum(time_spis2):
            if tovar1 < tovar2:
                tovar1 = tovar2 + 1
                if potrebnosti[day_num][tovar1] == 0:
                    continue
                time_spis1.append(proizvodstvo(num, tovar1)[1])
                tovari -= 1
                tovar_spis.append(tovar1 + 1)#Временная история, для отслеживания товаров
            else:
                tovar2 = tovar1 + 1
                if potrebnosti[day_num][tovar2] == 0:
                    continue
                time_spis2.append(proizvodstvo(num, tovar2)[1])
                tovari -= 1
                tovar_spis.append(tovar2 + 1)#Временная история, для отслеживания товаров
        elif sum(time_spis1) > sum(time_spis2):
            tovari -= 1
            tovar2 += 1
            if tovar2 == tovar1:
                tovar2 += 1
            num += 1
            if tovar2 > 9 or potrebnosti[day_num][tovar2] == 0:
                continue
            time_spis2.append(proizvodstvo(num, tovar2)[1])
            tovar_spis.append(tovar2 + 1)
        elif sum(time_spis1) < sum(time_spis2):
            tovari -= 1
            tovar1 = tovar2 + 1
            num += 1
            if tovar1 > 9 or potrebnosti[day_num][tovar1] == 0:
                continue
            time_spis1.append(proizvodstvo(num, tovar1)[1])
            tovar_spis.append(tovar1 + 1)
            if tovar1 - tovar2 > 0:
                tovar2 += 1

    day_num += 1
    tovar1 = 0
    tovar2 = 0

print(tovar_spis)
print(time_spis1)
print(time_spis2)
print(max((sum(time_spis2), sum(time_spis1))) / 24)