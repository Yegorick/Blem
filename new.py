from operator import rshift
from random import randint


proizvoditelnost = (1100, 1160, 1100, 1000, 1050, 1000, 1150, 1150, 1160, 1150)
day_3 = [22500, 0, 16500, 0, 2226, 0, 4600, 12450, 0, 0]
day_4 = [14015, 16250, 0, 0, 0, 0, 5400, 3800, 0, 0]
day_5 = [8200, 8200, 10100, 0, 0, 8200, 8200, 8200, 0, 3200]
day_6 = [12200, 14200, 8600, 0, 0, 12200, 0, 0, 0, 0]
day_10 = [23800, 34865, 25800, 0, 0, 30160, 8200, 34900, 4100, 9000]
day_12 = [0, 25100, 13150, 0, 0, 0, 6500, 0, 0, 0]
day_13 = [22500, 0, 16500, 0, 2226, 0, 4600, 12450, 0, 0]
day_15 = [22215, 24450, 10100, 0, 0, 8200, 13600, 12000, 0, 3200]
day_20 = [8200, 22700, 22300, 0, 0, 20300, 8200, 20400, 0, 3200]
day_23 = [22500, 0, 16500, 0, 2226, 0, 4600, 12450, 0, 0]
day_25 = [20400, 22400, 18700, 0, 0, 20400, 8200, 8200, 0, 3200]
day_26 = [14015, 16250, 0, 0, 0, 0, 5400, 3800, 0, 0]
day_28 = [12100, 25100, 13150, 0, 0, 0, 6500, 0, 0, 0]
day_30 = [8200, 22700, 22300, 0, 0, 20300, 8200, 20400, 0, 3200]
day_n = [46150, 16250, 41950, 9980, 0, 24400, 0, 42500, 9900, 9800]
potrebnosti = [day_3, day_4, day_5, day_6, day_10, day_12, day_13, day_15, day_20, day_23, day_25, day_26, day_28, day_30, day_n]
ostatki = [25670, 33830, 16400, 3550, 3600, 24550, 7800, 22780, 3600, 5260]

day_num = 0
num1 = 1
num2 = 1
tovar_spis = []
time_spis1 = []
time_spis2 = []
index = 0


def proizvodstvo(potrebnost, num, index):
    ost = potrebnost
    proizv = proizvoditelnost[index]
    main = potrebnost
    for i in range(10000):
        x = randint(0, 24)
        if num != 1:
            second = (main + 100) - (proizv * x)
            if second > -proizv:
                if second < ost:
                    ost = second
                    time = x + 1
        else:
            second = main - (proizv * x)
            if second > -proizv:
                if second < ost:
                    ost = second
                    time = x
    return (ost, time)


for day in potrebnosti:
    for i in day:
        if i == 0:
            index += 1
            continue
        else:
            if ostatki[index] - day[index] > 0:
                ostatki.insert(index, ostatki.pop(index) - day[index])
                tovar_spis.append(index + 1)
                index += 1
                continue
            else:
                day[index] -= ostatki[index]
                ostatki[index] = 0
            if num1 == 1:
                result = proizvodstvo(i, num1, index)
                time_spis1.append(result[1])
                print(result)
                ostatki[index] = result[0]
                num1 += 1
                tovar_spis.append(index + 1)
                index += 1
                continue
            if sum(time_spis1) == sum(time_spis2):
                result = proizvodstvo(i, num1, index)
                time_spis1.append(result[1])
                ostatki[index] = result[0]
                num1 += 1
            elif sum(time_spis1) < sum(time_spis2):
                result = proizvodstvo(i, num1, index)
                time_spis1.append(result[1])
                ostatki[index] = result[0]
                num1 += 1
            else:
                result = proizvodstvo(i, num2, index)
                time_spis2.append(result[1])
                ostatki[index] = result[0]
                num2 += 1
        tovar_spis.append(index + 1)
        index += 1
    index = 0
    day_num += 1

print(tovar_spis)
print(time_spis1)
print(time_spis2)
print(max(sum(time_spis1), sum(time_spis2)) / 24)
print(ostatki)
