proizvoditelnost = (1100, 1160, 1100, 1000, 1050, 1000, 1150, 1150, 1160, 1150)
day_3 = [22500, 0, 16500, 0, 2226, 0, 4600, 12450, 0, 0]
day_4 = [14015, 16250, 0, 0, 0, 0, 5400, 3800, 0, 0]
day_5 = [8200, 8200, 10100, 0, 0, 8200, 8200, 8200, 0, 3200]
potrebnosti = [day_3, day_4, day_5]
day_num = 0
for day in potrebnosti:
    for i in day:
        if i == 0:
            continue
        print(i)