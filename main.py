import random
pointsUser = 0
pointsPc = 0
repeat = int(input("Do ilu punktów gramy? "))
while pointsUser < repeat and pointsPc < repeat:
    user = int(input("1 - Kamień, 2 - Papier, 3 - Nożyce, wybierz: "))
    pc = random.randint(1,3)
    if user == 1:
        if pc == 1:
            print("Ty: Kamień, Komputer: Kamień --- REMIS")
        if pc == 2:
            print("Ty: Kamień, Komputer: Papier --- PRZEGRANA")
            pointsPc += 1
        if pc == 3:
            print("Ty: Kamień, Komputer: Nożyce --- WYGRANA")
            pointsUser += 1

    if user == 2:
        if pc == 1:
            print("Ty: Papier, Komputer: Kamień --- WYGRANA")
            pointsUser += 1
        if pc == 2:
            print("Ty: Papier, Komputer: Papier --- REMIS")
        if pc == 3:
            print("Ty: Papier, Komputer: Nożyce --- PRZEGRANA")
            pointsPc += 1

    if user == 3:
        if pc == 1:
            print("Ty: Nożyce, Komputer: Kamień --- PRZEGRANA")
            pointsPc += 1
        if pc == 2:
            print("Ty: Nożyce, Komputer: Papier --- WYGRANA")
            pointsUser += 1
        if pc == 3:
            print("Ty: Nożyce, Komputer: Nożyce --- REMIS")
    
    if user > 3 or user < 1:
        print("Nie możesz wybrać takiej opcji!")

if(pointsUser > pointsPc):
    print("Brawo! Wygrałeś!")
    print("Wynik:",pointsUser,":",pointsPc)
else:
    print("Niestety przegrałeś :(")
    print("Wynik:",pointsPc,":",pointsUser)
