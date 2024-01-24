def vytvor_trojuhelnik(rozmer):
    if rozmer % 2 == 0:
        rozmer += 1  # Zajisti, že počet sloupců je vždy lichý

    pole = [[' ' for _ in range(rozmer)] for _ in range(rozmer)]

    stred = rozmer // 2
    pole[0][stred] = '*'  # První hvězda uprostřed nultého řádku

    for radek in range(1, rozmer):
        for sloupec in range(rozmer):
            if sloupec > 0 and sloupec < rozmer - 1:
                pole[radek][sloupec] = pole[radek - 1][sloupec - 1] + pole[radek - 1][sloupec + 1]

    # Výpis trojúhelníka
    for radek in pole:
        print(' '.join(map(str, radek)).center(2 * rozmer - 1))

# Zadej libovolný rozmer (počet sloupců - lichý)
rozmer = int(input("Zadej rozmer trojúhelníka (lichý počet sloupců): "))
vytvor_trojuhelnik(rozmer)
