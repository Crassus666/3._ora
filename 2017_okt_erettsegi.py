#1. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\naplo.txt', 'r')

#2. feladat

sor_2 = txt.readline()
elso_karakter_2 = txt.read(1)
hianyzasok_szama = 0

while(elso_karakter_2!=""):

    if(elso_karakter_2 != "#" and elso_karakter_2 != ""):
        hianyzasok_szama += 1

    sor_2 = txt.readline()
    elso_karakter_2 = txt.read(1)

print("2. feladat")
print("A naplóban", hianyzasok_szama, "bejegyzés van")
txt.close()

#3. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\naplo.txt', 'r')

elso_karakter_3 = txt.read(1)
spacek_szama = 0
igazolt = 0
igazolatlan = 0
jelen = 0
hetig = 0

while(elso_karakter_3!=""):

    if(elso_karakter_3 != "#" and elso_karakter_3 != "" and spacek_szama != 2 and elso_karakter_3 != " "):
        elso_karakter_3 = txt.read(1)

    if spacek_szama == 2 and hetig <= 7:
        if elso_karakter_3 == "O":
            jelen += 1
        if elso_karakter_3 == "X":
            igazolt += 1
        if elso_karakter_3 == "I":
            igazolatlan += 1
        hetig += 1
        elso_karakter_3 = txt.read(1)


    if hetig == 7:
        hetig = 0
        spacek_szama = 0

    if elso_karakter_3 == " ":
        spacek_szama += 1
        elso_karakter_3 = txt.read(1)


    if elso_karakter_3 == "#":

        elso_karakter_3 = txt.read(6)
        spacek_szama = 0

print("3. feladat")
print(f'Az igazolt hiányzások száma {igazolt},', "az igazolatlanoké", igazolatlan, "óra.")
txt.close()

