from os import listdir
from os.path import isfile, join

fajlovi = []
podaci = []
dan = []
v = []
ime_prezime= []
provedeno_vreme = []

for f in listdir("python_v4/"):
    if isfile:
        fajlovi.append(join(f))

for i in fajlovi:
    f = open("python_v4/" + i,"r")
    for j in f:
        lista = [j.split(",")]
        dan = i[:-4]
        lista[0].append(dan)
        podaci.append(lista)
    f.close()

for k in podaci:
    for l in k:
        pocetno_vreme = l[1].split(":")
        min1 = int(pocetno_vreme[0]) * 60 + int(pocetno_vreme[1])
        krajnje_vreme = l[2].split(":")
        min2 = int(krajnje_vreme[0]) * 60 + int(krajnje_vreme[1])
        vreme = min2 - min1

        if vreme // 60 < 10:
            sati = "0" + str(vreme // 60)
        else:
            sati = str(vreme // 60)
        if vreme % 60 < 10:
            minuti = "0" + str(vreme % 60)
        else:
            minuti = str(vreme % 60)
        ukupno_provedeno_vreme = sati + ":" + minuti
        v.append([l[0],vreme])
        datum = ""
        for p in l[3]:
            if p == "_":
                datum += "."
            else:
                datum += p
                
        print("Radnik: " + l[0] + "; Vreme: " + ukupno_provedeno_vreme + "; Datum: " + datum)
      
for n in v:
    if n[0] not in ime_prezime:
        ime_prezime.append(n[0])
        provedeno_vreme.append(0)
        
for n in v:
    index = ime_prezime.index(n[0])
    provedeno_vreme[index]+= n[1]

for m in range(len(provedeno_vreme)):
    if provedeno_vreme[m] // 60 < 10:
        sati = "0" + str(provedeno_vreme[m] // 60)
    else:
        sati = str(provedeno_vreme[m] // 60)
    if provedeno_vreme[m] % 60 < 10:
        minuti = "0" + str(provedeno_vreme[m] % 60)
    else:
        minuti = str(provedeno_vreme[m] % 60)
    ukupno_provedeno_vreme = sati + ":" + minuti
    provedeno_vreme[m] = ukupno_provedeno_vreme

print(provedeno_vreme)
print(
"""
------------------------------------------------
""")
for o in range(len(provedeno_vreme)):
    print(ime_prezime[o] + ", " + provedeno_vreme[o])
print(
"""
------------------------------------------------
""")
