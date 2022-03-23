from random import randint


proizvoditelnost = (1100, 1160, 1100, 1000, 1050, 1000, 1150, 1150, 1160, 1150)
day_3 = [22500, 0, 16500, 0, 2226, 0, 4600, 12450, 0, 0]
day_4 = [14015, 16250, 0, 0, 0, 0, 5400, 3800, 0, 0]
day_5 = [8200, 8200, 10100, 0, 0, 8200, 8200, 8200, 0, 3200]
potrebnosti = [day_3, day_4, day_5]
#Если прокопировать day_5 и запустить с их учётом, не срабатывает 10 производство! Нужно фиксить

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
            if num1 == 1:
                time_spis1.append(proizvodstvo(i, num1, index)[1])
                num1 += 1
                tovar_spis.append(index + 1)
                index += 1
                continue
            if sum(time_spis1) == sum(time_spis2):
                time_spis1.append(proizvodstvo(i, num1, index)[1])
                num1 += 1
            elif sum(time_spis1) < sum(time_spis2):
                time_spis1.append(proizvodstvo(i, num1, index)[1])
                num1 += 1
            else:
                time_spis2.append(proizvodstvo(i, num2, index)[1])
                num2 += 1
        tovar_spis.append(index + 1)
        index += 1
    index = 0
    day_num += 1

print(tovar_spis)
print(time_spis1)
print(time_spis2)
print(max(sum(time_spis1), sum(time_spis2)) / 24)