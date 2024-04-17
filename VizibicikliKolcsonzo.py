class Kolcsonzo:
    def __init__(self,name,ids,sh,sm,eh,em):
        self.name = name
        self.ids = ids 
        self.sh = sh
        self.sm = sm 
        self.eh = eh
        self.em = em

    def __str__(self) -> str:
        return self.name, self.ids

file = open("kolcsonzesek.txt", "rt", encoding="utf-8")
kolcsonzesek = []
kolcson = []
idopont = []



for row in file:
   row = row.strip().split(";")
   kolcsonzesek.append(Kolcsonzo(row[0],row[1], row[2], row[3], row[4], row[5]))

print("5. feladat: Napi kölcsönzések száma:", len(kolcsonzesek)-1)

inputs = input("6. feladat: Kérek egy nevet:")
for i in kolcsonzesek:
    if inputs == i.name:
        idopont.append(int(i.sh))
        idopont.append(int(i.sm))
        idopont.append(int(i.eh))
        idopont.append(int(i.em)) 
        kolcson.append(idopont)
        idopont = []

if len(kolcson) > 0:    
    print(inputs, "kölcsönzései:")
    for i in kolcson: 
        if i[0] < 10:
            sh = f"0{i[0]}"
        else:
            sh = i[0]
        if i[1] < 10:
            sm = f"0{i[1]}"
        else:
            sm = i[1]
        if i[2] < 10:
            eh = f"0{i[2]}"
        else:
            eh = i[2]
        if i[3] < 10:
            em = f"0{i[3]}"
        else:
            em = i[3]
                
        print(f"{sh} : {sm} - {eh} : {em}")
else:
    print("Nem volt ilyen nevű kölcsonző!")