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
tovar1 = 0
tovar2 = 1
tovari = []


#def proizvodstvo(num, tovar):
#    ost = potrebnosti[day_num][tovar]
#    for i in range(10000):
#        main = potrebnosti[day_num][tovar]
#        x = randint(0, 24)
#        if num != 1:
#            second = (main + 100) - (proizvoditelnost[tovar] * x)
#            if second > -proizvoditelnost[tovar]:
#                if second < ost:
#                    ost = second
#                    time = x + 1
#        else:
#            second = main - (proizvoditelnost[tovar] * x)
#            if second > -proizvoditelnost[tovar]:
#                if second < ost:
#                    ost = second
#                    time = x
#    return (ost, time)

def proizvodstvo(potrebnost, num):
    ost = potrebnost
    proizv = proizvoditelnost[potrebnosti[day_num].index(potrebnost)]
    for i in range(10000):
        main = potrebnost
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
    #print(day)
    for i in day:
        if i == 0:
            tovar1 += 1
            tovar2 += 1
            continue
        else:
            if tovar1 > 9 or tovar2 > 9:
                break
            if num1 == 1:
                time_spis1.append(proizvodstvo(i, num1)[1])
                tovar1 += 1
                num1 += 1
                tovar_spis.append(potrebnosti[day_num].index(i) + 1)
                tovari.append('tovar1')
                continue
            if sum(time_spis1) == sum(time_spis2):
                print('!!!!!')
                time_spis1.append(proizvodstvo(i, num1)[1])
                tovar1 += 1
                num1 += 1
            elif sum(time_spis1) < sum(time_spis2):
                print(1)
                if tovari[-1] == 'tovar1':
                    tovar1 += 1
                else:
                    tovar1 = tovar2 + 1
                time_spis1.append(proizvodstvo(i, num1)[1])
                tovar1 += 1
                num1 += 1
                tovari.append('tovar1')
            else:
                print(2)
                if tovari[-1] == 'tovar2':
                    tovar2 += 1
                else:
                    tovar2 = tovar1 + 1
                time_spis2.append(proizvodstvo(i, num2)[1])
                tovar2 += 1
                num2 += 1
                tovari.append('tovar2')
        tovar_spis.append(potrebnosti[day_num].index(i) + 1)
    tovar1 = 0
    tovar2 = 0
    day_num += 1

print(tovar_spis)
print(time_spis1)
print(time_spis2)