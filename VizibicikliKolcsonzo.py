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
        idopont.append(i.sh)
        idopont.append(i.sm)
        idopont.append(i.eh)
        idopont.append(i.em) 
        kolcson.append(idopont)
        idopont = []

if len(kolcson) > 0:    
    print(inputs, "kölcsönzései:")
    for i in kolcson:
        print(f"{i[0]} : {i[1]} - {i[2]} : {i[3]}")
else:
    print("Nem volt ilyen nevű kölcsonző!")