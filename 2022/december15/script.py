dico_sensor_beacon = {}


with open("input.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.replace("Sensor at ", "")
        line = line.replace(": closest beacon is at", "")
        line = line.replace("\n", "")
        coord_list = line.split(", ")
        dico_sensor_beacon[(int(coord_list[0].replace("x=", "")), int(
            coord_list[1].replace("y=", "").split(" ")[0]))] = (int(
                coord_list[1].replace("x=", "").split(" ")[1]), int(coord_list[2].replace("y=", "")))


def cal_distance():
    dict_distance = {}
    for key in dico_sensor_beacon.keys():
        dict_distance[key] = abs(
            key[0] - dico_sensor_beacon[key][0]) + abs(key[1] - dico_sensor_beacon[key][1])
    return dict_distance


def calcul_couverture(couv1, couv2):
    x_start1, x_end1 = couv1
    x_start2, x_end2 = couv2
    if x_start1 <= x_end2 and (x_end1 >= x_start2 or x_start2 == x_end1 + 1) \
            or x_start2 <= x_end1 and (x_end2 >= x_start1 or x_start1 == x_end2 + 1):
        nouvelle_couverture = [[min(x_start1, x_start2), max(x_end1, x_end2)]]
        return nouvelle_couverture
    else:  # disjoints
        nouvelle_couverture = sorted([couv1, couv2], key=lambda x: x[0])
        return nouvelle_couverture


def couvertureLigneY(y):
    couverture_points = []
    d_distance = cal_distance()
    for key in d_distance.keys():
        ecart = abs(y - key[1])
        if ecart < d_distance[key]:
            x_min = key[0] - (d_distance[key] - ecart)
            x_max = key[0] + (d_distance[key] - ecart)
            couverture_senseur = [x_min, x_max]
            if not len(couverture_points):
                couverture_points.append(couverture_senseur)
            else:
                nouvelle_couverture_points = []
                for couverture in couverture_points:
                    couverture_sortie = calcul_couverture(
                        couverture, couverture_senseur)
                    if len(couverture_sortie) == 1:
                        # Si la couverture du senseur a été combinée, alors c'est la nouvelle range à tester
                        couverture_senseur = couverture_sortie[0]
                    else:
                        # Sinon, la première range est terminée, on attribut la seconde à couverture_senseur
                        nouvelle_couverture_points.append(couverture_sortie[0])
                        couverture_senseur = couverture_sortie[1]
                nouvelle_couverture_points.append(couverture_senseur)
                couverture_points = sorted(
                    nouvelle_couverture_points, key=lambda x: x[0])
    return couverture_points


def part_one_range(y):
    couverture = couvertureLigneY(y)[0]
    cases_prises = couverture[1] - couverture[0]
    # Retrait senseurs
    senseurRetires = []
    for key in dico_sensor_beacon.keys():
        if key[1] == y and couverture[0] <= key[0] <= couverture[1] + 1 and key not in senseurRetires:
            cases_prises -= 1
            senseurRetires.append(key)
    return cases_prises


def part_two_range(y_mini, y_maxi):
    for y in range(y_mini, y_maxi):
        couverture = couvertureLigneY(y)
        if len(couverture) > 1:
            x = couverture[0][1] + 1
            coef = x*4_000_000+y
            return coef


print(part_two_range(0, 4_000_000))
